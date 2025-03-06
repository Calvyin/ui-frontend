import flet as ft
import sys


def on_window_close(e):
    print("App is closing...")
    sys.exit()  # Ensures proper shutdown


def main(page: ft.Page):
    page.add(ft.Text("App Running..."))
    page.on_window_event = on_window_close


ft.app(target=main)
