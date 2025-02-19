import requests
import json

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

url = "https://llmapi-aiinfra.navinfo.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {credentials['deepseek-key']}"
}
data = {
    "model": "navinfo deepseek-r1",
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