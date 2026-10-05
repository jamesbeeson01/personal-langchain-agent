from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import uuid

from tools import list_directory, read_safe_file

system_prompt = """
You are a personal assistant. Be concise.
When asked about LangChain, always consult `docs_agent`.
Verify information in the files you can read before referencing them.
"""

agent = create_agent(
    model="google_genai:gemini-flash-lite-latest",
    tools=[read_safe_file, list_directory],
    checkpointer=InMemorySaver(),
)

thread_config = {"configurable": {"thread_id": uuid.uuid4()}}
def get_response(prompt: str) -> str:
    return agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        thread_config,
    )["messages"][-1].text