import datetime
from typing import Any, Protocol
from gov_proposals_explainer.clients import BaseHttpClient


class SenateOpenDataClient(Protocol):
    async def fetch_bill_type_list(self) -> list[dict[str, Any]]:
        ...

    async def fetch_bill_list(
        self,
        year: int = None,
        bill_type: str = None,
        number: int = None,
        author: str = None,
        keyword: str = None,
    ) -> list[dict[str, Any]]:
        ...

    async def fetch_bill_text(self, code: str) -> list[dict[str, Any]]:
        ...


class SenateOpenDataHttpClient(BaseHttpClient):
    async def fetch_bill_type_list(self) -> list[dict[str, Any]]:
        data = await self._fetch_data("/materia/subtipos")
        if not data:
            return []
        return (
            data.get("ListaSiglas", dict())
            .get("SiglasAtivas", dict())
            .get("Siglas", list())
        )

    async def fetch_bill_list(
        self,
        year: int = None,
        bill_type: str = None,
        number: int = None,
        author: str = None,
        keyword: str = None,
    ) -> list[dict[str, Any]]:
        params = {"ano": year or datetime.date.today().year}
        if bill_type:
            params["sigla"] = bill_type
        if number:
            params["numero"] = number
        if author:
            params["nomeAutor"] = author
        if keyword:
            params["palavraChave"] = keyword
        data = await self._fetch_data("/materia/pesquisa/lista", params=params)
        if not data:
            return []
        return (
            data.get("PesquisaBasicaMateria", dict())
            .get("Materias", dict())
            .get("Materia", list())
        )

    async def fetch_bill_text(self, code: str) -> list[dict[str, Any]]:
        data = await self._fetch_data(f"/materia/textos/{code}")
        if not data:
            return []
        return (
            data.get("TextoMateria", dict())
            .get("Materia", dict())
            .get("Textos", dict())
            .get("Texto", list())
        )
