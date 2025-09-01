from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientSession

class BaseHttpClient:
    def __init__(
        self,
        http_session: ClientSession,
        base_url: str = "https://legis.senado.leg.br/dadosabertos",
    ) -> None:
        self.base_url = base_url
        self.http_session = http_session
        self.http_session.headers.update({"accept": "application/json"})

    async def _fetch_data(
        self,
        endpoint: str,
        params: dict[str, Any] = None,
        headers: dict[str, str] = None,
    ) -> dict[str, Any]:
        async with self.http_session as session:
            async with session.get(
                f"{self.base_url}{endpoint}",
                headers=headers,
                params=params,
            ) as resp:
                if resp.status != 200:
                    print(f"Received unexpected status code: {resp.status}")
                    return {}
                data = await resp.json()
                return data