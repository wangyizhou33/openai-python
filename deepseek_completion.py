from openai import OpenAI
import json

# user should set `base_url="https://api.deepseek.com/beta"` to use this feature.
# expect credentials in a credentials.json' file
with open('credentials.json', 'r') as file:
    credentials = json.load(file)


# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    api_key=credentials["deepseek-key"],
    base_url="https://api.deepseek.com/beta"
)

response = client.completions.create(
  model="deepseek-chat",
  prompt="def fib(a):",
  suffix="    return fib(a-1) + fib(a-2)",
  max_tokens=128)
print(response.choices[0].text)