import flet as ft

def main(page: ft.Page):
    page.title = "My Mobile App"

    name = ft.TextField(
        label="Enter your name"
    )

    result = ft.Text()

    def click(e):
        result.value = f"Hello {name.value}!"
        page.update()

    page.add(
        ft.Text("My First App", size=25),
        name,
        ft.Button(
            content="Submit",
            on_click=click
        ),
        result
    )
ft.run(main)