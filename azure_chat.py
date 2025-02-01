from openai import AzureOpenAI
import json

# expect credentials in a credentials.json' file
with open('credentials.json', 'r') as file:
    credentials = json.load(file)

api_version = "2024-08-01-preview"

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    api_version=api_version,
    api_key=credentials["azure-chatgpt-key"],
    azure_endpoint="https://wyzgpt4.openai.azure.com",
)

completion = client.chat.completions.create(
    model="gpt-4o",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())

deployment_client = AzureOpenAI(
    api_version=api_version,
    api_key=credentials["azure-chatgpt-key"],
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://wyzgpt4.openai.azure.com",
    # Navigate to the Azure OpenAI Studio to deploy a model.
    azure_deployment="gpt-4o",  # e.g. gpt-35-instant
)

completion = deployment_client.chat.completions.create(
    model="<ignored>",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())