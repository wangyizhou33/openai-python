from ollama import Client
import json

with open('credentials.json', 'r') as file:
    credentials = json.load(file)


client = Client(
  host=credentials["ollama-url"],
  headers={'x-some-header': 'some-value'}
)

res = client.embed(
    model="llama3.2",
    input="The sky is blue because of rayleigh scattering",
)
print(res)
