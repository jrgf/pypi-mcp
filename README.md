# Pypi MCP

Pypi MCP is a Python project that provides a tool to retrieve package information from PyPI. It uses the FastMCP framework to define tools and dependencies.

## Features
- Retrieve the latest version, name, requirements, license, and summary of a package from PyPI.

## Requirements
- Python 3.10 or higher
- `requests` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jrgf/pypi-mcp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pypi-mcp
   ```
3. Install uv package manager :
   
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
4. Install mcp-cli:
    ```bash
    uv add "mcp[cli]"
    ```

## Running the Server
To start the server in dev mode, run the following command:
```bash
uv run mcp dev server.py
```
## Claude Desktop
To install the server in your Claude Desktop, run the following command:
```bash
uv run mcp install server.py
```


## Contribution Guidelines
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request to the main repository.

Please ensure your code follows the project's coding standards and includes tests where applicable.

## License
This project is licensed under the MIT License.