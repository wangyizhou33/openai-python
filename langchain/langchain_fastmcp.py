from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from model import load_azure_model, load_public_deepseek_model

model = load_public_deepseek_model()


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["/home/yizhouw/Repositories/openai/fastmcp/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        math_response["messages"][-1].pretty_print()
        weather_response = await agent.ainvoke(
            {"messages": "what is the weather in nyc?"}
        )
        weather_response["messages"][-1].pretty_print()


# To execute the asynchronous main function
import asyncio

asyncio.run(main())
