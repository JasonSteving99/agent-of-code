import atexit
from dataclasses import dataclass
from datetime import datetime
import enum
import duckdb
import os
from pathlib import Path
from pydantic import BaseModel
from result import Err, Ok, Result
from typing import Awaitable, Callable, Literal, ParamSpec, TypeVar, cast
from functools import wraps


@dataclass
class LLMUsageLoggingConfig:
    @dataclass
    class LoggingEnabledConfig:
        log_file: Path
        execution_id: int

    execution_name: str
    persisted_logs_config: LoggingEnabledConfig | None
    # TODO(steving) Add support for a max cost threshold. Could be useful to have a max threshold
    # for a single program execution, or also for a single overall task.


_CONFIG: LLMUsageLoggingConfig = None  # type: ignore


def configure_llm_usage_logging(execution_name: str, log_dir: os.PathLike | None) -> None:
    """Configure LLM Usage Logging.

    log_path: Path to the log file. If None, logs will only be printed to stdout but won't be
            persisted anywhere for later analysis.
    """
    global _CONFIG
    if log_dir is None:
        _CONFIG = LLMUsageLoggingConfig(
            execution_name=execution_name,
            persisted_logs_config=None,
        )
        return  # We're not actually persisting logs this time.

    log_file = Path(os.path.join(log_dir, "llm_usage.db"))
    with duckdb.connect(log_file) as conn:
        conn.execute(
            """
            CREATE SEQUENCE IF NOT EXISTS execution_id_sequence START 1;
            
            -- Always create a new subtask sequence since this should be incrementing within a program execution.
            DROP SEQUENCE IF EXISTS subtask_id_sequence;
            CREATE SEQUENCE subtask_id_sequence START 1;

            CREATE TABLE IF NOT EXISTS llm_usage (
                -- Globally incrementing program execution count - should be from `execution_id_sequence` above.
                execution_id INTEGER NOT NULL,
                -- Descriptive name of the current program execution.
                execution_name VARCHAR NOT NULL,
                -- A subtask is a single LLM call.
                subtask_id INTEGER NOT NULL DEFAULT nextval('subtask_id_sequence'),
                -- A descriptive name for a specific subtask (LLM call).
                subtask_name VARCHAR NOT NULL,
                start_timestamp TIMESTAMP NOT NULL,
                end_timestamp TIMESTAMP NOT NULL,
                -- The vendor (company) providing the LLM API or local model used for the current subtask.
                provider VARCHAR NOT NULL,
                -- The specific model name used for the current subtask.
                model VARCHAR NOT NULL,
                input_tokens INTEGER NOT NULL,
                -- If the LLM call was successful, this will be NULL. Otherwise, there will be an error message.
                output_tokens INTEGER,
                -- If the LLM encountered an error, then error and error_msg will be set.
                error VARCHAR DEFAULT NULL,
                error_msg VARCHAR DEFAULT NULL,

                PRIMARY KEY(execution_id, subtask_id),
                CHECK (error IS NULL or error_msg IS NOT NULL)
            );
            """  # noqa: E501
        )

        # The current program execution should be running with a single execution_id for all LLM
        # calls so that they can be associated together in the future.
        curr_execution_id = conn.execute(
            """
            SELECT nextval('execution_id_sequence');
            """
        ).fetchall()[0][0]
        _CONFIG = LLMUsageLoggingConfig(
            execution_name=execution_name,
            persisted_logs_config=LLMUsageLoggingConfig.LoggingEnabledConfig(
                log_file=log_file,
                execution_id=curr_execution_id,
            ),
        )

    atexit.register(_show_usage_summary)


def _show_usage_summary():
    """Show a summary of LLM usage."""
    if _CONFIG.persisted_logs_config is None:
        return

    print("\nLLM usage summary:")
    with duckdb.connect(_CONFIG.persisted_logs_config.log_file) as conn:
        conn.sql(
            "SELECT * FROM llm_usage WHERE execution_id = $1;",
            params=[_CONFIG.persisted_logs_config.execution_id],
        ).show()
        # Finally, cleanup the task id sequence since we'll want a new one next time.
        conn.execute("DROP SEQUENCE subtask_id_sequence;")


class LLMError(BaseModel):
    """Base class for all LLM errors."""

    class ErrType(enum.StrEnum):
        NO_RESPONSE = "NO_RESPONSE"
        UNEXPECTED_RESPONSE = "UNEXPECTED_RESPONSE"
        RESPONSE_SCHEMA_VALIDATION_FAILED = "RESPONSE_SCHEMA_VALIDATION_FAILED"
        LOGICAL_VALIDATION_FAILED = "LOGICAL_VALIDATION_FAILED"

    err_type: ErrType

    msg: str


class Model(enum.StrEnum):
    DYNAMIC_MODEL_CHOICE = "**DYNAMIC_MODEL_CHOICE**"


@dataclass
class LLMUsage[T]:
    input_tokens: int
    output_tokens: int
    response: Result[T, LLMError]

    def map[U](self, func: Callable[[T], U]) -> "LLMUsage[U]":
        return LLMUsage[U](
            input_tokens=self.input_tokens,
            output_tokens=self.output_tokens,
            response=(
                Ok(func(self.response.unwrap()))
                if self.response.is_ok()
                else Err(self.response.unwrap_err())
            ),
        )


def _has_required_str_kwarg(argname: str, func: Callable) -> bool:
    return argname in func.__annotations__ and (
        func.__annotations__[argname] is str
        or (
            isinstance(func.__annotations__[argname], type)
            and issubclass(func.__annotations__[argname], enum.StrEnum)
        )
    )


P = ParamSpec("P")
R = TypeVar("R")


def log_llm_usage(provider: str, model: str | Literal[Model.DYNAMIC_MODEL_CHOICE]):
    def decorator(
        func: Callable[P, Awaitable[LLMUsage[R]]],
    ) -> Callable[P, Awaitable[Result[R, LLMError]]]:
        if model == Model.DYNAMIC_MODEL_CHOICE and (
            not _has_required_str_kwarg(argname="model", func=func)
        ):
            raise ValueError(
                "If @log_llm_usage(..., model=LLMUsage.Model.DYNAMIC_MODEL_CHOICE), then the function must have a `model` argument of type str or subclass of enum.StrEnum."  # noqa: E501
            )
        if not _has_required_str_kwarg(argname="subtask_name", func=func):
            raise ValueError(
                "Functions wrapped with @log_llm_usage(...) must take a `subtask_name` argument of type str or subclass of enum.StrEnum."  # noqa: E501
            )

        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[R, LLMError]:
            if _CONFIG is None:
                raise ValueError(
                    f"Must call {configure_llm_usage_logging.__name__}(...) to configure LLM usage tracking."  # noqa: E501
                )

            start_timestamp = datetime.now()
            result = await func(*args, **kwargs)
            end_timestamp = datetime.now()

            # If the model is dynamic, then we need to extract it from the arguments.
            curr_model: str
            match model:
                case Model.DYNAMIC_MODEL_CHOICE:
                    curr_model = cast(str, kwargs["model"])
                case _:
                    curr_model = model

            # Get the subtask name.
            subtask_name = cast(str, kwargs["subtask_name"])

            if _CONFIG.persisted_logs_config:
                with duckdb.connect(_CONFIG.persisted_logs_config.log_file) as conn:
                    conn.execute(
                        """
                        INSERT INTO llm_usage (
                            execution_id,
                            execution_name,
                            subtask_name, 
                            start_timestamp,
                            end_timestamp,
                            provider,
                            model, 
                            input_tokens, 
                            output_tokens,
                            error,
                            error_msg
                        )
                        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);
                        """,
                        (
                            _CONFIG.persisted_logs_config.execution_id,
                            _CONFIG.execution_name,
                            subtask_name,
                            start_timestamp,
                            end_timestamp,
                            provider,
                            curr_model,
                            result.input_tokens,
                            result.output_tokens,
                            (
                                None
                                if result.response.is_ok()
                                else result.response.unwrap_err().err_type
                            ),
                            None if result.response.is_ok() else result.response.unwrap_err().msg,
                        ),
                    )

            return result.response

        return wrapper

    return decorator


async def test() -> None:
    # TESTING
    @log_llm_usage(provider="OpenAI", model="gpt-3.5-turbo")
    async def foo(*, subtask_name: str) -> LLMUsage[str]:
        # Simulating LLM usage
        import random
        from time import sleep

        sleep(random.randint(1, 300) / 1000)
        input_tokens = 100
        output_tokens = 50
        response = "This is a sample response"
        return LLMUsage(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            # response=Ok(response),
            response=Err(LLMError(err_type=LLMError.ErrType.NO_RESPONSE, msg="No response.")),
        )

    class TestModel(enum.StrEnum):
        MODEL_A = "model-a"
        MODEL_B = "model-b"

    @log_llm_usage(provider="FAKE PROVIDER", model=Model.DYNAMIC_MODEL_CHOICE)
    async def bar[ResType](
        *, model: TestModel, subtask_name: str, res: ResType
    ) -> LLMUsage[ResType]:
        return LLMUsage(
            input_tokens=50,
            output_tokens=10,
            response=Ok(res),
        )

    # Configuring the logging.
    configure_llm_usage_logging(
        execution_name="MyTask",
        log_dir=Path("."),
    )
    # Calling the decorated function
    await foo(subtask_name="foo")
    result = await foo(subtask_name="foo")
    await bar(model=TestModel.MODEL_A, subtask_name="bar", res=10)
    print(result)  # Outputs: This is a sample response


if __name__ == "__main__":
    import asyncio

    asyncio.run(test())
