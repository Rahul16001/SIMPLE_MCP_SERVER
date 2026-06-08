from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Simple MCP Server")

from pydantic import Field
from mcp.server.fastmcp.prompts import base

@mcp.tool(
    name="Check Armstrong number",
    description="Check if a number is an Armstrong number.",
)
def check_armstrong_number(
    n: int = Field(description="The number to check"),
):
    """An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153."""
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n


if __name__ == "__main__":
    mcp.run(transport="streamable-http")


