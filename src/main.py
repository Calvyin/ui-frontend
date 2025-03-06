import flet as ft
import sys


def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Container 1"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.PURPLE_200,
                    width=150,
                    height=75,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Function here")  # insert function here
                ),

                ft.Container(
                    content = ft.Text("Container 2"),
                    margin = 10,
                    padding = 10,
                    alignment = ft.alignment.center,
                    bgcolor = ft.Colors.GREEN_200,
                    width = 150,
                    height = 75,
                    border_radius = 10,
                    ink = True,
                    on_click = lambda e: print("Function here")  # insert function here
                ),

                ft.Container(
                    content = ft.Text("Container 3"),
                    margin = 10,
                    padding = 10,
                    alignment = ft.alignment.center,
                    bgcolor = ft.Colors.RED_200,
                    width = 150,
                    height = 75,
                    border_radius = 10,
                    ink = True,
                    on_click = lambda e: print("Function here")  # insert function here
                )
            ],
            alignment = "center"  # Centers elements horizontally
        )
    )


ft.app(main)
