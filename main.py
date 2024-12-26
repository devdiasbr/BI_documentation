import flet as ft
import logging
from src.ui.app import main
from src.utils.config import LOG_FILE, LOG_FORMAT

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    ft.app(target=main)
