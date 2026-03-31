"""
Application principale DomoHouse System.
"""
from tkinter import *
from ui.main_window import MainWindow

class App:
    def __init__(self):
        self.root = Tk()
        self.main_window = MainWindow(self.root)

    def run(self):
        self.root.mainloop()