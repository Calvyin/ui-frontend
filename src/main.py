import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(  # Center the Column itself
            content=ft.Column(
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
                        on_click=lambda e: print("Function here")
                    ),
                    ft.Container(
                        content=ft.Text("Container 2"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.GREEN_200,
                        width=150,
                        height=75,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print("Function here")
                    ),
                    ft.Container(
                        content=ft.Text("Container 3"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.RED_200,
                        width=150,
                        height=75,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print("Function here")
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Center items within Column
            ),
            alignment=ft.alignment.center,  # Center the entire Column on the screen
        )
    )


ft.app(target=main)
