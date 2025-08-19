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

@server.tool()
def divide(a: float, b: float) -> float:
    """
    Divides a by b, and returns the result.

    :param a: Numerator
    :param b: Denominator
    :return: Quotient of a and b

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

@server.tool()
def power(base: float, exponent: float) -> float:
    """
    Raises base to the power of exponent, and returns the result.

    :param base: Base number
    :param exponent: Exponent
    :return: Result of base ** exponent
    """
    return base ** exponent

@server.tool()
def mod(a: float, b: float) -> float:
    """
    Returns the remainder of a divided by b.

    :param a: Dividend
    :param b: Divisor
    :return: Remainder of a / b

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a % b

@server.tool()
def sqrt(a: float) -> float:
    """
    Returns the square root of a.

    :param a: Input number
    :return: Square root of a

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return a ** 0.5
