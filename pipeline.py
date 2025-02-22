from ollama import Client
import json
from openai import OpenAI

vision_client = Client(
  host='http://10.41.0.98:11434',
  headers={'x-some-header': 'some-value'}
)

response = vision_client.chat(
	model="llama3.2-vision:latest",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image',
			'images': ['./sample1.png']
		}
	]
)
print(response.message.content)


with open('credentials.json', 'r') as file:
    credentials = json.load(file)

# gets API Key from environment variable OPENAI_API_KEY
answer_client = OpenAI(
    api_key=credentials["deepseek-key"],
    base_url="https://llmapi-aiinfra.navinfo.com/v1"
)

system_prompt = "You are a classifier. Summarize the paragraph below and give me a unique class label. \
                 The available class labels are: \
                 CAR,VAN,TRUCK,TRAILER,BUS,ONRAILS,SCOOTER,KICK SCOOTER,RICKSHAW,PICKUP,PERSON,ANIMAL,VEGETATION,NONE_OF_ABOVE. \
                 Also tell me how confident you are in your answer, on a scale of 0 to 1. \
                 Write me a python code block, \
                 classification=<your_answer> \
                 confidence=<your_confidence> \
                 "

user_query = f"What's the main subject of this paragraph: {response.message.content}"

# Streaming:
print("----- streaming request -----")
stream = answer_client.chat.completions.create(
  model="navinfo deepseek-r1",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_query
        }
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
print()