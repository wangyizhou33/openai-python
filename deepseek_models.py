from openai import OpenAI
import json

# expect credentials in a credentials.json' file
with open('credentials.json', 'r') as file:
    credentials = json.load(file)

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(
    api_key=credentials["public-deepseek-key"],
    base_url=credentials["public-deepseek-url"]
)
print(client.models.list())