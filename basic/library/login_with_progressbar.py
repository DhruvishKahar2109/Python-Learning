from rich.console import Console
from rich.progress import Progress
import time

console = Console()

username = input("Please enter your username: ")
password = input("Please enter your password: ")

#correct username and password

correct_username = "admin"
correct_password = "admin@123"

with Progress() as progress:
     task = progress.add_task("[cyan]Checking Login...", total=100)

     for x in range(100):
         time.sleep(0.02)
         progress.update(task, advance=1)

# Authentication
if username == correct_username and password == correct_password:
    console.print("[bold green]✓ Login Successfully![/bold green]")
else:
    console.print("[bold red]✗ Invalid username or password![/bold red]")