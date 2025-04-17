from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# load OPENAI_API_KEY env var
load_dotenv()

llm = AzureChatOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint="https://wyzgpt4.openai.azure.com",
    azure_deployment="gpt-4o",  # e.g. gpt-35-instant
)


system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

print(f"prompt: {prompt}")
print(f"prompt_to_message: {prompt.to_messages()}")

response = llm.invoke(prompt)
response.pretty_print()
