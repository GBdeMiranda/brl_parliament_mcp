# BRAZILIAN CONGRESS MCP

## Overview

This project provides an interface to interact with the legislative data of the Brazilian Congress.

## Usage

1. Install the MCP tool in editable mode:
`uv tool install -e .`

2. Add your servers in the mcpServers key
```
    "mcp_brl_congress": {
        "command": "mcp_brl_congress"
    }
```

3. Restart your MCP client to apply the changes.

4. Test the integration by sending a request to the MCP server. For instance:
```
Explique o PL 2630 de 2020 do senado brasileiro.
```
