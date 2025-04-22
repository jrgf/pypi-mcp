from mcp.server.fastmcp import FastMCP
import requests


mcp = FastMCP("Pypi MCP",dependencies=["requests"])


@mcp.tool()
def retrieve_package_info(name: str):
    """
    Retrieve package information from PyPI"
    """
    try:
        response = requests.get(f"https://pypi.org/pypi/{name}/json")
        if response.status_code == 200:
            return {
                "latest_version": response.json()["info"]["version"],
                "name": response.json()["info"]["name"],
                "requirements": response.json()["info"]["requires_dist"],
                "license": response.json()["info"]["license"],
                "summary": response.json()["info"]["summary"],  
            }
        else:
            print(f"Package {name} not found.")
            return None
    except Exception as e:
        print(f"Error retrieving package info: {e}")
        return None

if __name__ == "__main__":
    mcp.run()