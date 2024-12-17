import atexit
from dataclasses import dataclass
from datetime import datetime
import enum
import duckdb
import os
from pathlib import Path
from pydantic import BaseModel
from result import Err, Result
from typing import Callable, Any
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
    if _CONFIG:
        raise Exception(f"Already configured logging!\n{_CONFIG}")

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
        VALIDATION_FAILED = "VALIDATION_FAILED"

    err_type: ErrType

    msg: str


@dataclass
class LLMUsage[T]:
    input_tokens: int
    output_tokens: int
    response: Result[T, LLMError]


def log_llm_usage(provider: str, model: str):
    def decorator[T](func: Callable[..., LLMUsage[T]]) -> Callable[..., Result[T, LLMError]]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Result[T, LLMError]:
            start_timestamp = datetime.now()
            if _CONFIG is None:
                raise ValueError(
                    f"Must call {configure_llm_usage_logging.__name__}(...) to configure LLM usage tracking."  # noqa: E501
                )

            result = func(*args, **kwargs)
            end_timestamp = datetime.now()

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
                            func.__name__,
                            start_timestamp,
                            end_timestamp,
                            provider,
                            model,
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


if __name__ == "__main__":
    # TESTING
    @log_llm_usage(provider="OpenAI", model="gpt-3.5-turbo")
    def foo() -> LLMUsage[str]:
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

    # Configuring the logging.
    configure_llm_usage_logging(
        execution_name="MyTask",
        log_dir=Path("."),
    )
    # Calling the decorated function
    foo()
    result = foo()
    print(result)  # Outputs: This is a sample response
