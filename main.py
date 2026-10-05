from dotenv import load_dotenv
load_dotenv()

from commands import commands
from main_agent import get_response
from error_handler import setup_exception_hook

from rich.console import Console
from rich.markdown import Markdown
from rich.rule import Rule

console = Console()


def main():
    setup_exception_hook()
    # 1/0 # test error handler
    while True:
        console.print(Rule("[bold cyan]USER[/]", characters="━", style = "cyan"))
        try:
            prompt = input("Input: ")

            if prompt in commands: 
                commands[prompt]()
                continue

            response = get_response(prompt)
        except (EOFError, SystemExit):
            break

        console.print(Rule("[bold green]AI[/]", characters="━", style = "green"))
        console.print(Markdown(response))
    

if __name__ == "__main__":
    main()
