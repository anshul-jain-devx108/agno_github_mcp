from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters
from dotenv import load_dotenv

# Load .env file
load_dotenv()

async def run_agent(message: str) -> None:
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-github"],
    )

    async with MCPTools(server_params=server_params,timeout_seconds=30) as mcp_tools:
        agent = Agent(
            model=Gemini(id="gemini-2.0-flash"),  # Use Gemini instead of default OpenAI
            tools=[mcp_tools],
            instructions="You are a GitHub assistant...",
            markdown=True,
        )
        
        response = await agent.arun(message)
        return response


