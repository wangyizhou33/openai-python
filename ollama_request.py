import requests
import json

url = "http://localhost:7869/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "llama3.2",
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