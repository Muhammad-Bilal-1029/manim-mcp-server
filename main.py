import random
from fastmcp import FastMCP

mcp = FastMCP(name="first_mcp_server")


@mcp.tool
def simple_calculator(a: float, b: float, operator: str) -> float:
    """
    Perform a basic arithmetic operation on two numbers.

    Supported operators: + - * / ** % //
    """
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            return a / b
        case "**":
            return a ** b
        case "%":
            if b == 0:
                raise ValueError("Cannot perform modulo by zero.")
            return a % b
        case "//":
            if b == 0:
                raise ValueError("Cannot perform floor division by zero.")
            return a // b
        case _:
            raise ValueError(
                f"Unsupported operator: {operator!r}. Use one of + - * / ** % //"
            )

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

# -----------------------------------------------------------------------
# NOTES: making this server reachable REMOTELY (i.e. from outside your PC)
# -----------------------------------------------------------------------
# host="0.0.0.0" already means "listen on every network interface", so
# anyone on your local WiFi/LAN can reach it via http://<your-lan-ip>:8000
# But your LAN IP is NOT reachable from the public internet by default.
#
# Two common ways to actually expose it remotely:
#
# 1) Quick tunnel with ngrok (good for testing, no cloud account needed):
#       - Install ngrok: https://ngrok.com/download
#       - In one terminal:  python server.py
#       - In another terminal:  ngrok http 8000
#       - ngrok gives you a public URL like https://abcd1234.ngrok-free.app
#         Anyone can hit that URL and it forwards to your local server.
#
# 2) Deploy on a cloud VM (permanent/production use):
#       - Spin up a VM (DigitalOcean, AWS EC2, GCP, Azure, etc.)
#       - Copy server.py + requirements to the VM (scp/git clone)
#       - pip install fastmcp
#       - Open port 8000 in the VM's firewall / security group
#       - Run:  python server.py   (or use nohup / systemd / tmux so it
#         keeps running after you close the SSH session)
#       - Access via http://<vm-public-ip>:8000
# -----------------------------------------------------------------------