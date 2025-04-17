from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# load OPENAI_API_KEY env var
load_dotenv()

model = AzureChatOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint="https://wyzgpt4.openai.azure.com",
    azure_deployment="gpt-4o",  # e.g. gpt-35-instant
)

print("--------------  Example of no history  --------------")
print(model.invoke([HumanMessage(content="Hi! I'm Bob")]).content)
print(model.invoke([HumanMessage(content="What's my name?")]).content)


workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

query = "Hi! I'm Bob."

input_messages = [HumanMessage(query)]
config = {"configurable": {"thread_id": "abc123"}}
output = app.invoke({"messages": input_messages}, config)

print("--------------  Example of history  --------------")
output["messages"][-1].pretty_print()
query = "What's my name?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()
