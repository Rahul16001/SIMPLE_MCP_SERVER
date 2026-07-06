# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A minimal MCP (Model Context Protocol) server built with FastMCP, exposing tools that can be called by MCP clients (e.g. Claude Code, Claude Desktop). Currently exposes a single tool, `check_armstrong_number`, in `armstrong_mcp_server.py`.

## Environment

- Python >=3.13, managed with `uv` (see `pyproject.toml` and `uv.lock`).
- Dependency management is done through `uv`, not pip directly.

## Commands

```bash
# Install dependencies / sync the virtual environment
uv sync

# Run the MCP server (HTTP transport, defaults to port 10000, override with PORT env var)
uv run armstrong_mcp_server.py
```

There are no tests, lint config, or build steps in this repo currently.

## Architecture

- The server is created with `FastMCP("My Simple MCP Server")`.
- Tools are registered via the `@mcp.tool(...)` decorator directly above their function definition. Each tool uses `pydantic.Field` to document its parameters, which FastMCP surfaces to MCP clients as part of the tool schema.
- The server runs over `http` transport, binding to `0.0.0.0` and reading the port from the `PORT` environment variable (default `10000`) — this matches deployment on platforms like Render that inject `PORT`.
- To add a new tool: define a function, decorate it with `@mcp.tool(name=..., description=...)`, and use `Field(description=...)` on parameters that need explanation. The function's docstring can add further detail (as done for the Armstrong number tool).
