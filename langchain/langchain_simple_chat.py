from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# load OPENAI_API_KEY env var
load_dotenv()

llm = AzureChatOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint="https://wyzgpt4.openai.azure.com",
    azure_deployment="gpt-4o",  # e.g. gpt-35-instant
)

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]
# Equivalent to
# model.invoke("hi")
# model.invoke([{"role": "user", "content": "hi"}])
# model.invoke([HumanMessage("hi")])

response = llm.invoke(messages)
print(response.content)
