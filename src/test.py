import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Stack(
            [
                ft.Container(bgcolor=ft.colors.GREY_300, width=300, height=200),  # Background
                ft.Container(ft.Text("Top Left"), bgcolor=ft.colors.RED, width=100, height=50, left=0, top=0),
                ft.Container(ft.Text("Bottom Right"), bgcolor=ft.colors.BLUE, width=100, height=50, right=0, bottom=0)
            ]
        )
    )

ft.app(target=main)
