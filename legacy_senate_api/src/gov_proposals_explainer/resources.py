from aiohttp import ClientSession
from gov_proposals_explainer.clients import SenateOpenDataHttpClient


async def senate_client() -> SenateOpenDataHttpClient:
    senate_client = SenateOpenDataHttpClient(http_session=ClientSession())
    return senate_client
