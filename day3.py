# Create a logic gate game.

from rich import print # import rich CLI tools 
from rich.console import Console
console = Console()
from rich.prompt import Prompt
import questionary

console.rule("[bold magenta] :trident: Treasure Island Adventure :trident: [/bold magenta]")
console.print("Your mission is to find the treasure. Make wise choices!\n", style="italic")

direction = console.input("[bold cyan]Do you go [green]Left[/green] or [red]Right[/red]?[/bold cyan] :compass: ").lower()

if direction != 'left':
    print('You fell into a hole. \ Game over.')
    quit()
    
# Q2 - 
console.print("[bold blue]You're at a river. What will you do?[/bold blue]")
choice = questionary.select(
    "Choose your action:",
    choices=["Swim", "Wait"],
).ask()
if choice.lower() != 'wait':
    print('You drowned :water: - suck it!')
    quit()

# Q3 - Door colour
console.print("Choose a door color: [bold red]red[/bold red], [bold yellow]yellow[/bold yellow], [bold blue]blue[/bold blue], [bold green]green[/bold green], [bold magenta]purple[/bold magenta].")
door = Prompt.ask("Which colour door?", choices=['red', 'yellow', 'blue', 'green', 'purple']).lower()

if door == 'red':
    print('Burned by fire. Game over.')
    console.print(" :fire: Burned by fire. [bold red]Game over.[/bold red]", style="red")
    quit()
    
elif door == 'blue':
    console.print(":zombie: Eaten by beasts. [bold blue]Game over.[/bold blue]", style="blue")
    quit()

elif door == 'yellow':
    console.print(":gold: [bold yellow]You found the treasure! You win![/bold yellow]", style="yellow")
    quit()
        
else:
    print('Game over!')
    quit()
    
