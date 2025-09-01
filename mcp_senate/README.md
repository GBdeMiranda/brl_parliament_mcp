# BRAZILIAN PARLIAMENT MCP

## Overview

This project provides an interface to interact with the Brazilian Parliament's legislative data.

## Usage

1. Install dependencies:
`uv add mcp[cli] httpx PyMuPDF`

2. Add your servers in the mcpServers key
```
    "brazil_senate": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/FOLDER",
        "run",
        "mcp_server.py"
      ]
    }
```

3. Run MCP Server:
`uv run mcp_server.py`

4. Restart your MCP client to apply the changes.

5. Test the integration by sending a request to the MCP server. For instance:
```
Explique o PL 2630 de 2020 do senado brasileiro.
```


