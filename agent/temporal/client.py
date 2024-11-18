from temporalio.client import Client
from agent import settings


async def get_temporal_client() -> Client:
    # TODO(steving) Generalize this to enable running locally or against prod Temporal Cloud.
    return await Client.connect(
        f"{settings.TEMPORAL_HOST}:{settings.TEMPORAL_PORT}",
        namespace=settings.TEMPORAL_NAMESPACE,
        rpc_metadata={"temporal-namespace": settings.TEMPORAL_NAMESPACE},
        api_key=settings.TEMPORAL_API_KEY,
        tls=isinstance(settings.TEMPORAL_API_KEY, str),
    )
