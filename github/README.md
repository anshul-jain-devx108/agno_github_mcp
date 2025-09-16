# GitHub Assistant API

This project is a FastAPI-based web service that provides an endpoint to interact with a Google Gemini-powered AI assistant specialized for GitHub-related tasks.

It uses the **Agno Agent Framework** to structure the AI agent and the **Model Context Protocol (MCP)** to securely provide the agent with context from a local GitHub repository.

## Core Technologies

*   **[Agno](https://github.com/phidata/phidata):** An open-source Python framework for building high-performance, model-agnostic AI agents and multi-agent systems. It provides the structure for defining the agent's tools, memory, and reasoning capabilities.
*   **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/):** An open standard that enables AI applications to connect with external data sources and tools. In this project, it's used to create a bridge between the agent and a local GitHub repository server (`@modelcontextprotocol/server-github`), allowing the agent to access file contents, directory structures, and other repository information.
*   **[FastAPI](https://fastapi.tiangolo.com/):** A modern, fast (high-performance) web framework for building APIs with Python.
*   **[Google Gemini](https://deepmind.google/technologies/gemini/):** The `gemini-2.0-flash` model is used for its powerful and efficient language processing capabilities.

## Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

*   Python 3.9+
*   [Node.js and npm](https://nodejs.org/en/download/) (for the MCP GitHub server)
*   An active Google AI (Gemini) API Key.
*   A GitHub Personal Access Token.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd github
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a file named `.env` in the root of the project. This file will hold your secret keys.

    You need to add:
    *   A **Google AI API Key** to authenticate with the Gemini model.
    *   A **GitHub Personal Access Token** for the MCP server to access your repository data.

    Your `.env` file should look like this:
    ```env
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    GITHUB_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN_HERE"
    ```
    *To create a GitHub token, go to [github.com/settings/tokens](https://github.com/settings/tokens) and generate a new token with the appropriate permissions (e.g., `repo` scope for private repositories).*

### Running the Application

The `run.py` script will start the `uvicorn` server, which in turn runs the FastAPI application. The application is configured to automatically launch the MCP GitHub server.

```sh
python run.py
```

The API will be available at `http://localhost:8000`.

### Testing the API

You can test the API using a tool like [Postman](https://www.postman.com/) or by visiting the interactive documentation provided by FastAPI.

#### Option 1: Using Postman

1.  **Create a new request:** Open Postman and create a new HTTP request.
2.  **Set the method and URL:**
    *   Change the HTTP method to `POST`.
    *   Enter the following URL: `http://localhost:8000/query/`
3.  **Add the query parameter:**
    *   Go to the "Params" tab.
    *   Add a new parameter:
        *   **KEY:** `message`
        *   **VALUE:** `Explain the purpose of the app.py file`
4.  **Send the request:** The body of the request can be left empty. Click the "Send" button.

You should see the JSON response from the agent in the response panel below.

#### Option 2: Using FastAPI's Interactive Docs

A major advantage of FastAPI is its automatic interactive documentation.

1.  **Run the application:** Make sure the server is running (`python run.py`).
2.  **Open your browser:** Navigate to `http://localhost:8000/docs`.
3.  **Test the endpoint:**
    *   You will see the API documentation. Find the `/query/` endpoint and expand it.
    *   Click the "Try it out" button.
    *   Enter your message (e.g., `Explain the purpose of the app.py file`) in the `message` field.
    *   Click the "Execute" button.

The documentation page will show you the live response from the server.

## Project Structure

*   `main.py`: Defines the FastAPI application and the `/query/` endpoint.
*   `app.py`: Contains the core agent logic, including `agno` agent initialization, `mcp` tool configuration, and interaction with the Gemini model.
*   `run.py`: A simple script to start the `uvicorn` server for development.
*   `requirements.txt`: Lists the Python dependencies for the project.
*   `.env`: Holds environment variables like API keys. **(This file is not committed to version control)**.
*   `.gitignore`: Specifies files and directories to be ignored by Git.

## How to Contribute

Contributions are welcome! If you have a suggestion or find a bug, please open an issue to discuss it.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request