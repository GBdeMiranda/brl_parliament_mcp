import io
from typing import Any, Iterator
import httpx
from mcp.server.fastmcp import FastMCP
import fitz  # PyMuPDF

import logging  # stderr

mcp = FastMCP("senate")

API_BASE_URL = "https://legis.senado.leg.br/dadosabertos"

async def make_senate_request(url: str) -> dict[str, Any] | None:
    """Make a request to the Senate API for JSON data."""
    headers = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0, follow_redirects=True)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

async def fetch_pdf_content(url: str) -> bytes | None:
    """Make a request to fetch raw PDF content."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0, follow_redirects=True)
            response.raise_for_status()
            return response.content
        except Exception:
            return None

def find_document_urls(data: dict) -> Iterator[str]:
    """Recursively find all 'UrlDocumento' values in the nested JSON response."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "urlDocumento" and isinstance(value, str):
                yield value
            else:
                yield from find_document_urls(value)
    elif isinstance(data, list):
        for item in data:
            yield from find_document_urls(item)

@mcp.tool()
async def getBillText(number: str, year: str) -> str:
    """
    Get the text of a legislative bill from the Brazilian Senate.

    Args:
        number: The number of the bill.
        year: The year of the bill.
    """

    # -----------------------------------------------------
    process_url = f"{API_BASE_URL}/processo.json?numero={number}&ano={year}"
    process_data = await make_senate_request(process_url)

    if not process_data:
        return f"Could not find a legislative process for bill {number}/{year}."
    

    # -----------------------------------------------------
    doc_urls = list(find_document_urls(process_data))
    if not doc_urls:
        return "Found the legislative process, but it has no associated documents."


    # -----------------------------------------------------
    # Fetch and extract text from each document
    all_extracted_text = []
    for doc_url in doc_urls:
        pdf_bytes = await fetch_pdf_content(doc_url)
        if pdf_bytes:
            try:
                # In-memory stream
                with fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf") as doc:
                    full_text = "".join(page.get_text() for page in doc)
                if full_text.strip():
                    all_extracted_text.append(full_text)
            except Exception:
                # Silent fail
                continue
    
    if not all_extracted_text:
        return "Found documents, but could not extract any text. They may be empty or image-based."

    return "\n\n--- (New Document) ---\n\n".join(all_extracted_text)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
