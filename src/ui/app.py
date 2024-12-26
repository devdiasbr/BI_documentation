import flet as ft
from pathlib import Path
from src.ui.components.main_window import MainWindow

def main(page: ft.Page):
    """
    Função principal que inicializa a aplicação Flet.
    
    Args:
        page (ft.Page): Objeto Page do Flet
    """
    MainWindow(page)
