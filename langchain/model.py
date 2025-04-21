from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_openai import ChatOpenAI
import json


def load_azure_model():
    load_dotenv()
    model = AzureChatOpenAI(
        api_version="2024-08-01-preview",
        azure_endpoint="https://wyzgpt4.openai.azure.com",
        azure_deployment="gpt-4o",  # e.g. gpt-35-instant
    )
    return model


def load_public_deepseek_model():
    with open("credentials.json", "r") as file:
        credentials = json.load(file)

    model = ChatOpenAI(
        base_url=credentials["public-deepseek-url"],
        api_key=credentials["public-deepseek-key"],
        model="deepseek-chat",
    )
    return model

def load_private_deepseek_model():
    with open("credentials.json", "r") as file:
        credentials = json.load(file)

    model = ChatOpenAI(
        base_url=credentials["llmapi-url"],
        api_key=credentials["llmapi-key"],
        model="navinfo deepseek-v3",
    )
    return model