from openai import OpenAI

import json

# expect credentials in a credentials.json' file
with open('credentials.json', 'r') as file:
    credentials = json.load(file)


# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    api_key=credentials["deepseek-key"],
    base_url="https://llmapi-aiinfra.navinfo.com/v1"
)

# # Non-streaming:
# print("----- standard request -----")
# completion = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I output all files in a directory using Python in short?",
#         },
#     ],
# )
# print(completion.choices[0].message.content)


# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
  model="navinfo deepseek-v3",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
print()

