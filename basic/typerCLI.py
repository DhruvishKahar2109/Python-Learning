import typer

app = typer.Typer()

@app.command()
def main(name: str):
    print(f"Hello {name}!")

@app.command()
def add(a: int, b: int):
    print(a + b)

if __name__ == "__main__":
    app()