from ollama import Client

client = Client(
  host='http://localhost:7869',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(
    model='llama3.2', 
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
])
print(response.message.content)

response = client.chat(
	model="llama3.2-vision:11b",
	messages=[
		{
			'role': 'user',
			'content': 'where is this',
			'images': ['./beijing.png']
		}
	]
)
print(response.message.content)
