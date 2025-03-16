import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core.workflow import Context
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv

load_dotenv()

# Embedding model
ollama_embedding = OllamaEmbedding(
    model_name="nomic-embed-text:latest",
    base_url="http://10.41.0.98:11434",
)

llm = AzureOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint="https://wyzgpt4.openai.azure.com",
    azure_deployment="gpt-4o",  # e.g. gpt-35-instant
)

Settings.embed_model = ollama_embedding
Settings.llm = llm

# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("llama_index_data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# index can be saved,
# https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/#storing-the-rag-index


# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about an personal essay written by Paul Graham."""
    response = await query_engine.aquery(query)
    return str(response)


# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    name="Agent",
    description="Useful for multiplying two numbers",
    tools=[multiply, search_documents],
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)


async def main():
    # create context
    ctx = Context(agent)

    # Run the agent
    response = await agent.run("What is 1234 * 4567?")
    print(str(response))

    # run agent with RAG
    response = await agent.run("What is IPD?")
    print(str(response))

    # run agent with context
    response = await agent.run("My name is Yizhou", ctx=ctx)
    print(str(response))
    response = await agent.run("What is my name?", ctx=ctx)
    print(str(response))


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
