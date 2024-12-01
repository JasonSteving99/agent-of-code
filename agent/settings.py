from os import environ

AOC_COOKIE: str
match environ.get("AOC_COOKIE"):
    case str(cookie):
        AOC_COOKIE = cookie
    case _:
        raise RuntimeError("You must set the AOC_COOKIE env variable!")

ANTHROPIC_API_KEY: str
match environ.get("ANTHROPIC_API_KEY"):
    case str(api_key):
        ANTHROPIC_API_KEY = api_key
    case _:
        raise RuntimeError("Must set ANTHROPIC_API_KEY env variable!")

GEMINI_API_KEY: str
match environ.get("GEMINI_API_KEY"):
    case str(api_key):
        GEMINI_API_KEY = api_key
    case _:
        raise RuntimeError("Must set GEMINI_API_KEY env variable!")

TEMPORAL_HOST = "localhost"  # TODO: Need different val for dev/prod.
TEMPORAL_PORT = "7233"
TEMPORAL_NAMESPACE = "default"  # TODO: Need different val for dev/prod.
TEMPORAL_API_KEY: str | None = None  # TODO: Should use an api key in prod and not in dev.
TEMPORAL_TASK_QUEUE_NAME = "advent-of-code-agent-task-queue"
