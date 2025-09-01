from typing import Any
from gov_proposals_explainer import clients, schemas


async def get_senate_bill_types(
    senate_client: clients.SenateOpenDataClient,
) -> list[dict[str, Any]]:
    bill_types = await senate_client.fetch_bill_type_list()
    return bill_types


async def get_senate_bills(
    senate_client: clients.SenateOpenDataClient,
    bill_specs: schemas.BillParams,
) -> list[dict[str, Any]]:
    bills = await senate_client.fetch_bill_list(
        year=bill_specs.year,
        bill_type=bill_specs.bill_type,
        number=bill_specs.number,
        author=bill_specs.author,
        keyword=bill_specs.keyword,
    )
    return bills


async def get_senate_bill(
    senate_client: clients.SenateOpenDataClient, bill_code: schemas.BillCode
) -> list[dict[str, Any]]:
    bill = await senate_client.fetch_bill_text(bill_code.code)
    return bill
