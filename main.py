# build local mcp server
import random
from typing import List
from fastmcp import FastMCP

mcp = FastMCP(name= "first_mcp_server")

@mcp.tool
def multiply_number(a:float , b:float) -> float:
    """multiply two numbers together """
    return   a * b

@mcp.tool  # decorator
def add_number(a:float , b:float) -> float:
    """add two numbers together """
    addition = a + b
    return addition

@mcp.tool
def roll_dice(n_dice : int = 1)->list[int]:
    """roll n_dice 6 sides and return the result"""
    return [random.randint(1,6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", =8000) 

