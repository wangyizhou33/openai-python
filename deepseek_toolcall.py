from openai import OpenAI

import json

# expect credentials in a credentials.json' file
with open("credentials.json", "r") as file:
    credentials = json.load(file)


def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat", messages=messages, tools=tools
    )
    print("print here ", response.choices[0].message)
    return response.choices[0].message


# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    api_key=credentials["public-deepseek-key"],
    base_url=credentials["public-deepseek-url"],
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of an location, the user shoud supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"],
            },
        },
    },
]

messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

tool = message.tool_calls[0]
messages.append(message)

messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})
message = send_messages(messages)
print(f"Model>\t {message.content}")
