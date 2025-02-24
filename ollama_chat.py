from ollama import Client
import json

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

client = Client(
  host=credentials["ollama-url"],
  headers={'x-some-header': 'some-value'}
)
response = client.chat(
    model='llama3.2-vision', 
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
])
print(response.message.content)

response = client.chat(
	model="llama3.2-vision",
	messages=[
		{
			'role': 'user',
			'content': 'where is this',
			'images': ['./beijing.png']
		}
	]
)
print(response.message.content)
