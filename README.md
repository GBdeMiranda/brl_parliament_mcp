# Brazilian Parliament MCP Server

An MCP (Model Context Protocol) server that provides access to Brazilian Parliament legislative data, specifically enabling retrieval and analysis of Senate bills and legislative documents.

## Overview

This project provides a standardized interface to interact with the Brazilian Senate's open data API through the Model Context Protocol. It allows users to fetch detailed information about legislative bills, including their full text content extracted from PDF documents.

### Key Features

- **Bill Text Retrieval**: Fetch complete text content of Brazilian Senate bills
- **PDF Processing**: Automatic extraction of text from legislative documents
- **MCP Integration**: Seamless integration with MCP-compatible clients
- **Real-time Data**: Access to up-to-date legislative information from the Senate's official API

## Project Structure

```
brl_parliament_mcp/
├── mcp_senate/           # Main MCP server implementation
│   ├── mcp_server.py     # Core MCP server with bill retrieval functionality
│   ├── pyproject.toml    # Project dependencies and configuration
│   ├── uv.lock          # Dependency lock file
│   └── README.md        # Component-specific documentation
├── legacy_senate_api/    # Legacy Flask-based API (deprecated)
│   ├── src/             # Source code for legacy implementation
│   ├── requirements.txt # Legacy dependencies
│   └── readme.md        # Legacy documentation
└── README.md            # This file
```

## Installation

### Prerequisites

- Python 3.13 or higher
- UV package manager (recommended) or pip

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GBdeMiranda/brl_parliament_mcp.git
   cd brl_parliament_mcp
   ```

2. **Navigate to the MCP server directory**:
   ```bash
   cd mcp_senate
   ```

3. **Install dependencies**:
   
   Using UV (recommended):
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install mcp[cli] httpx PyMuPDF
   ```

## Usage

### Running the MCP Server

To start the MCP server locally:

```bash
cd mcp_senate
uv run mcp_server.py
```

### MCP Client Integration

To integrate this server with an MCP client, add the following configuration to your MCP client's settings:

```json
{
  "mcpServers": {
    "brazil_senate": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/brl_parliament_mcp/mcp_senate",
        "run",
        "mcp_server.py"
      ]
    }
  }
}
```

Replace `/absolute/path/to/brl_parliament_mcp/mcp_senate` with the actual absolute path to the mcp_senate directory on your system.

### Available Tools

#### `getBillText`

Retrieves the complete text content of a Brazilian Senate bill.

**Parameters**:
- `number` (string): The bill number
- `year` (string): The year the bill was proposed

**Example Usage**:
```
Explain PL 2630 from 2020 from the Brazilian Senate.
```

This will automatically:
1. Query the Senate's API for the legislative process
2. Find all associated documents
3. Download and extract text from PDF files
4. Return the combined text content

## API Details

The server connects to the official Brazilian Senate open data API:
- **Base URL**: `https://legis.senado.leg.br/dadosabertos`
- **Data Format**: JSON responses with PDF document links
- **Document Processing**: Automatic PDF text extraction using PyMuPDF

## Examples

### Basic Bill Lookup

To get information about a specific bill:

```python
# This would be sent to the MCP server
getBillText(number="2630", year="2020")
```

The server will:
1. Search for the legislative process
2. Extract all associated documents
3. Download and process PDF files
4. Return the complete bill text

### Integration with AI Assistants

This MCP server is designed to work seamlessly with AI assistants that support the MCP protocol. Once configured, you can ask natural language questions like:

- "What is PL 2630/2020 about?"
- "Show me the text of bill 1234 from 2023"
- "Explain the main points of the internet regulation bill"

## Development

### Legacy Components

The `legacy_senate_api` directory contains an older Flask-based implementation that is kept for reference but is not actively maintained. The current focus is on the MCP-based implementation in the `mcp_senate` directory.

### Contributing

When contributing to this project:

1. Focus on the `mcp_senate` directory for new features
2. Ensure compatibility with MCP protocol standards
3. Test with actual Senate API endpoints
4. Update documentation for any new tools or features

## Technical Details

### Dependencies

- **mcp[cli]**: Model Context Protocol implementation
- **httpx**: Modern HTTP client for API requests
- **PyMuPDF**: PDF processing and text extraction
- **Python 3.13+**: Required for modern async/await support

### Error Handling

The server includes robust error handling for:
- Network timeouts and connection issues
- Invalid bill numbers or years
- PDF processing failures
- API response parsing errors

### Performance Considerations

- Async/await pattern for non-blocking operations
- Efficient PDF text extraction
- Connection pooling for HTTP requests
- Graceful handling of large documents

## License

This project interfaces with public data from the Brazilian Senate's official open data API. Please ensure compliance with the Senate's terms of service when using this tool.

## Support

For issues, questions, or contributions, please use the GitHub repository's issue tracker.