# Brazilian Congress MCP Server

An MCP (Model Context Protocol) server that provides access to Brazilian Parliament legislative data, specifically enabling the retrieval and analysis of Senate bills and legislative documents.

## Installation

### Prerequisites

- Python 3.10+
- UV package manager (recommended) or pip

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GBdeMiranda/brl_parliament_mcp.git
   cd brl_parliament_mcp
   ```

2. **Navigate to the MCP server directory**:
   ```bash
   cd mcp_brl_congress
   ```

3. **Install the MCP tool**:
  ```bash
  uv tool install -e .
  ```

4. Add your servers in the mcpServers key
```
    "mcp_brl_congress": {
        "command": "mcp_brl_congress"
    }
```


## Usage

Restart your MCP client to apply the changes.

### MCP Client Integration

To integrate this server with an MCP client, add the following configuration to your MCP client's settings:

```json
    "mcp_brl_congress": {
        "command": "mcp_brl_congress"
    }
```

### Testing the Integration

Send a request to the MCP server. For instance:
```
Explique o PL 2630 de 2020 do senado brasileiro.
```

## API Details

The server connects to the official Brazilian Senate open data API:
- **Base URL**: `https://legis.senado.leg.br/dadosabertos`
- **Data Format**: JSON responses with PDF document links
- **Document Processing**: Automatic PDF text extraction using PyMuPDF

### Integration with AI Assistants

This MCP server is designed to work seamlessly with AI assistants that support the MCP protocol. Once configured, you can ask natural language questions like:

- "What is PL 2630/2020 about?"
- "Show me the text of bill 1234 from 2023"
- "Explain the main points of the internet regulation bill" (WiP)

## Development

### Contributing

When contributing to this project:

1. Ensure compatibility with MCP protocol standards
2. Test with actual Senate API endpoints
3. Update documentation for any new tools or features


## Dependencies

- **mcp[cli]**: Model Context Protocol implementation
- **httpx**: Modern HTTP client for API requests
- **PyMuPDF**: PDF processing and text extraction
- **Python 3.10+**: Required for modern async/await support

## Terms of Use

This project interfaces with public data from the Brazilian Senate's official open data API. Please ensure compliance with the Senate's terms of service when using this tool.
