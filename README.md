
# Project Title

A brief description of what this project does and who it's for

# Calculator MCP Server

This is a sample **MCP Server in Python** implementing calculator tools.  
It can be used as a scaffold for your own MCP Server.  
It includes the following features:  

- **Basic Arithmetic Tools**: Add, subtract, multiply, divide.  
- **Advanced Math Tools**: Power, modulus, and square root.  
- **Error Handling**: Safe checks for division by zero and invalid inputs (e.g., square root of negative numbers).  
- **Connect to Agent Builder**: Allows you to connect the MCP server to the Agent Builder for testing and debugging.  
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Test and debug the MCP Server with an interactive interface.  

---

## Get started with the Calculator MCP Server

> **Prerequisites**
>
> To run the MCP Server in your local dev machine, you will need:
>
> - [Python](https://www.python.org/)  
> - (*Optional - if you prefer uv*) [uv](https://github.com/astral-sh/uv)  
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)  

---

## Prepare environment

There are two approaches to set up the environment for this project. You can choose either one:

| Approach | Steps |
| -------- | ----- |
| Using `uv` | 1. Create virtual environment: `uv venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and select the python from created virtual environment <br>3. Install dependencies (include dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Using `pip` | 1. Create virtual environment: `python -m venv .venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and select the python from created virtual environment<br>3. Install dependencies (include dev dependencies): `pip install -e .[dev]` |  

---

## Run the Calculator Server

After setting up the environment, you can run the server in your local dev machine via Agent Builder as the MCP Client:

1. Open VS Code Debug panel. Select `Debug in Agent Builder` or press `F5` to start debugging the MCP server.  
2. Use AI Toolkit Agent Builder to test the server with a prompt such as:  


The server will automatically connect to the Agent Builder and return the result.  
3. Click `Run` to test the server with the prompt.  

✅ **Congratulations!** You have successfully run the Calculator MCP Server in your local dev machine via Agent Builder.  

![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

---

## What's included in the template

| Folder / File| Contents                                         |
| ------------ | ------------------------------------------------ |
| `.vscode`    | VSCode files for debugging                       |
| `.aitk`      | Configurations for AI Toolkit                    |
| `src`        | The source code for the calculator MCP server    |

---

## Tools Implemented

| Tool       | Description                                     | Notes |
|------------|-------------------------------------------------|-------|
| `add`      | Adds two numbers                                | - |
| `subtract` | Subtracts one number from another               | - |
| `multiply` | Multiplies two numbers                          | - |
| `divide`   | Divides a by b                                  | Raises `ZeroDivisionError` if b=0 |
| `power`    | Raises base to exponent                         | - |
| `mod`      | Returns the remainder of a / b                  | Raises `ZeroDivisionError` if b=0 |
| `sqrt`     | Returns the square root of a                    | Raises `ValueError` if input < 0 |

---

## Debugging Options

### Agent Builder  
- Debug the MCP server in the Agent Builder via AI Toolkit.  
- Example: `What is 5 * 8?`  

### MCP Inspector  
- Install [Node.js](https://nodejs.org/)  
- Setup Inspector:
    ```bash
    cd inspector
    npm install
    ```
- Debug in VS Code: Select Debug SSE in Inspector (Edge/Chrome) and press F5.
- In MCP Inspector (browser): click Connect, list tools, provide inputs, and run tests.

---

### Default Ports and Customization

| Debug Mode	| Ports	| Config Files |
|---------------|-------|--------------|
| Agent Builder	| 3001	| launch.json, tasks.json, mcp.json |
| MCP Inspector	| 3001 (Server); 5173 and 3000 (Inspector)	| Same as above |
