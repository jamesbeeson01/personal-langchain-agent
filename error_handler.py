import sys
from langchain.agents import create_agent

from rich.console import Console 
from rich.markdown import Markdown 

console = Console()

def custom_excepthook(exc_type, exc_value, exc_traceback):
    print("\n-------- ERROR --------")
    
    agent = create_agent("google_genai:gemini-flash-lite-latest")

    prompt = f"""
        Explain this error:
        - exc_type: {exc_type}
        - exc_value: {exc_value}
        - exc_traceback: {exc_traceback}
    """
    
    response = agent.invoke({
        "messages": [{
                "role": "user",
                "content": prompt,
            }]
        }
    )["messages"][-1].text

    console.print(Markdown(response))

    print("\nExiting...\n")

def setup_exception_hook():
    sys.excepthook = custom_excepthook