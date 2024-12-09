from os import environ

from google.cloud import secretmanager_v1


GCLOUD_PROJECT_ID: str | None = environ.get("GCLOUD_PROJECT_ID")


def _get_secret(name: str) -> str:
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()
    # Make the request
    response = client.access_secret_version(
        request=secretmanager_v1.AccessSecretVersionRequest(
            name=f"projects/{GCLOUD_PROJECT_ID}/secrets/{name}/versions/latest",
        )
    )
    return response.payload.data.decode("utf-8")


AOC_COOKIE: str
match environ.get("AOC_COOKIE"):
    case str(cookie):
        AOC_COOKIE = cookie
    case _:
        if GCLOUD_PROJECT_ID:
            AOC_COOKIE = _get_secret("aoc-cookie")
        else:
            raise RuntimeError("You must set the AOC_COOKIE env variable!")

ANTHROPIC_API_KEY: str
match environ.get("ANTHROPIC_API_KEY"):
    case str(api_key):
        ANTHROPIC_API_KEY = api_key
    case _:
        if GCLOUD_PROJECT_ID:
            ANTHROPIC_API_KEY = _get_secret("anthropic-api-key")
        else:
            raise RuntimeError("Must set ANTHROPIC_API_KEY env variable!")

GEMINI_API_KEY: str
match environ.get("GEMINI_API_KEY"):
    case str(api_key):
        GEMINI_API_KEY = api_key
    case _:
        if GCLOUD_PROJECT_ID:
            GEMINI_API_KEY = _get_secret("gemini-api-key")
        else:
            raise RuntimeError("Must set GEMINI_API_KEY env variable!")

OPENAI_API_KEY: str
match environ.get("OPENAI_API_KEY"):
    case str(api_key):
        OPENAI_API_KEY = api_key
    case _:
        if GCLOUD_PROJECT_ID:
            OPENAI_API_KEY = _get_secret("openai-api-key")
        else:
            raise RuntimeError("Must set OPENAI_API_KEY env variable!")

TEMPORAL_HOST = "localhost"  # TODO: Need different val for dev/prod.
TEMPORAL_PORT = "7233"
TEMPORAL_NAMESPACE = "default"  # TODO: Need different val for dev/prod.
TEMPORAL_API_KEY: str | None = None  # TODO: Should use an api key in prod and not in dev.
TEMPORAL_TASK_QUEUE_NAME = "advent-of-code-agent-task-queue"
