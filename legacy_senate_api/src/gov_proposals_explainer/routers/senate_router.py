from typing import Annotated
from fastapi import APIRouter, Depends
from gov_proposals_explainer import resources, services, clients, schemas

router = APIRouter(prefix="/senate")


@router.get("/bill_types")
async def get_senate_bill_types(
    senate_client: Annotated[
        clients.SenateOpenDataClient, Depends(resources.senate_client)
    ]
) -> list[schemas.BillType]:
    bill_types = await services.get_senate_bill_types(senate_client)
    return bill_types


@router.get("/bills")
async def get_senate_bills(
    senate_client: Annotated[
        clients.SenateOpenDataClient, Depends(resources.senate_client)
    ],
    year: int | None = None,
    bill_type: str | None = None,
    number: int | None = None,
    author: str | None = None,
    keyword: str | None = None,
) -> list[schemas.BillSpecs]:
    bill_specs = schemas.BillParams(
        year=year, bill_type=bill_type, number=number, author=author, keyword=keyword
    )
    senate_bills = await services.get_senate_bills(senate_client, bill_specs)
    return senate_bills


@router.get("/bill")
async def get_senate_bill(
    senate_client: Annotated[
        clients.SenateOpenDataClient, Depends(resources.senate_client)
    ],
    code: str,
) -> list[schemas.BillText]:
    bill_code = schemas.BillCode(code=code)
    bill = await services.get_senate_bill(senate_client, bill_code)
    return bill
