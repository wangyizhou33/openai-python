import requests
import json

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

url = credentials["azure-chatgpt-url"] + "/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
headers = {
    "Content-Type": "application/json",
    "api-key": f"{credentials['azure-chatgpt-key']}"
}
data = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print(response.json())  # Convert response to JSON and print
