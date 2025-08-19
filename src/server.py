"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("calculator")

@server.tool()
def add(a: float, b: float) -> float:
    """
    Adds two numbers together, and return the result.

    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """
    Subtracts b from a, and returns the result.

    :param a: First number
    :param b: Second number
    :return: Difference of a and b
    """
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers together, and returns the result.

    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b
