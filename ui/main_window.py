from tkinter import *
from ui.components.menu import Menu
from config import ColorConfig
from ui.frames.dashboard_frame import Dashboard


class MainWindow:
    def __init__(self, root_):
        col = ColorConfig()

        self.root = root_
        self.root.title("DomoHouse System")
        self.root.geometry("1024x600")
        self.root.configure(bg=col.primary_white)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_rowconfigure(0, weight=1)

        self.menu_frame = Menu(root_)
        self.dashboard_frame = Dashboard(root_)