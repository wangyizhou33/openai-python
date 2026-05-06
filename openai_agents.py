import asyncio
import json
from agents import Agent, Runner, RunConfig, OpenAIProvider, function_tool, handoff

@function_tool
def history_fun_fact() -> str:
    """Return a short history fact."""
    return "Sharks are older than trees."

with open("credentials.json", "r") as file:
    credentials = json.load(file)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You answer history questions clearly and concisely.",
    model="deepseek-chat",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You explain math step by step and include worked examples.",
    model="deepseek-chat",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Route each homework question to the right specialist.",
    handoffs=[
        handoff(history_tutor_agent, tool_name_override="transfer_to_history_tutor"),
        handoff(math_tutor_agent, tool_name_override="transfer_to_math_tutor"),
    ],
    model="deepseek-chat",
)

run_config = RunConfig(
    model_provider=OpenAIProvider(
        api_key=credentials["public-deepseek-key"],
        base_url=credentials["public-deepseek-url"],
        use_responses=False,
    ),
    tracing_disabled=True,  # otherwise will get `OPENAI_API_KEY is not set, skipping trace export`
)

async def main():
    result = await Runner.run(
        triage_agent,
        "Who was the first president of the United States?",
        run_config=run_config,
    )
    print(result.final_output)
    print(f"Answered by: {result.last_agent.name}")

if __name__ == "__main__":
    asyncio.run(main())
