from ollama import Client

client = Client(
    host="http://localhost:7869",
    headers={"x-some-header": "some-value"},
)

res = client.embed(
    model="llama3.2",
    input="The sky is blue because of rayleigh scattering",
)
print(res)
