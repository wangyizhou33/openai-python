from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import StructuredTool, Tool
import requests


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


def get_weather(latitude, longitude) -> str:
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    print(data["current"]["temperature_2m"])
    return str(data["current"]["temperature_2m"])


def save_to_file(data: str, filename: str = "result.txt"):

    with open(filename, "a", encoding="utf-8") as f:
        f.write(data)

    return f"Data successfully save to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_file,
    description="Save answer to a text file",
)


class WeatherInput(BaseModel):
    latitude: float = Field(description="latitude of the place of interest")
    longitude: float = Field(description="longitude of the place of interest")


weather_tool = StructuredTool.from_function(
    name="weather",
    func=get_weather,
    description="query weather from the internet",
    # args_schema=WeatherInput,  # Specify the input schema
)
tools = [weather_tool, save_tool]

load_dotenv()

llm = AzureChatOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint="https://wyzgpt4.openai.azure.com",
    azure_deployment="gpt-4o",  # e.g. gpt-35-instant
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions} 
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = "What's the weather in Shanghai now? Save the result to file"
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output"))
except Exception as e:
    print("Error parsing response", e, "Raw response - ", raw_response)
