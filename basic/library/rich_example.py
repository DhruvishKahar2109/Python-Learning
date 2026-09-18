from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

table = Table(title = "Employee Details")
table.add_column("Name")
table.add_column("Salary")
table.add_column("Department")

table.add_row("Dhruvish","29","Python Developer")
table.add_row("Raj","32","Designer")
table.add_row("Rohan","28","HR")

console.print(table)
for x in track(range(100), description="Employee Details ..."):
    time.sleep(1)



# print("[green]Sucess![/green]")
# print("[red]Errror![/red]")
# print("[yellow]Warning![/yellow]")