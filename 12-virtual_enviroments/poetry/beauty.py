from rich.console import Console
from rich.text import Text
import time

consola = Console()

message = Text("Beauty is in the eye of the beholder", style="bold magenta")

for letra in message:
    consola.print(letra, end="", style="bold magenta")
    time.sleep(0.1)


