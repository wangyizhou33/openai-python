from ollama import Client
import json
import requests


def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


# expect credentials in a credentials.json' file
with open("credentials.json", "r") as file:
    credentials = json.load(file)

client = Client(host=credentials["ollama-url"], headers={"x-some-header": "some-value"})
model = "llama3.1:8b"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for provided coordinates in celsius.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

messages = [{"role": "user", "content": "What's the weather like in Paris today?"}]

completion = client.chat(
    model=model,
    messages=messages,
    tools=tools,
)

print(completion.message.tool_calls)

tool_call = completion.message.tool_calls[0]

print("Calling function:", tool_call.function.name)
print("Arguments:", tool_call.function.arguments)
result = get_weather(**tool_call.function.arguments)
print("Function output:", get_weather(**tool_call.function.arguments))

messages.append(completion.message)  # append model's function call message
messages.append(
    {  # append result message
        "role": "tool",
        "content": str(result),
        "name": tool_call.function.name,
    }
)
print(messages)

completion_2 = client.chat(
    model=model,
    messages=messages,
    tools=tools,
)
print(completion_2.message.content)
