from tkinter import *
from PIL import ImageTk, Image
from config import ColorConfig, FontFamilyConfig

class Menu:
    def __init__(self, root_):
        self.root = root_

        col = ColorConfig()
        ff = FontFamilyConfig(self.root)

        self.menu_frame = Frame(self.root, width=400, padx=24, pady=32, bg=col.neutral_white)
        self.menu_frame.grid(row=0, column=0, sticky='nsew')

        image = Image.open(fp="assets/icons/icon_house.png")
        image = ImageTk.PhotoImage(image.resize((32, 32)))

        self.home_wrapper = Frame(self.menu_frame, bg=col.neutral_white)
        self.home_wrapper.pack(anchor="w", fill="x")

        self.home_icon = Label(self.home_wrapper, image=image, bg=col.neutral_white)
        self.home_icon.image = image
        self.home_icon.grid(row=0, column=0)

        self.home_text = Label(
            self.home_wrapper, text=str.upper("DomoHouse System"),
            font=(ff.text_title, 18, "bold"), bg=col.neutral_white,
            padx=16
        )
        self.home_text.grid(row=0, column=1)

        self.menu_wrapper = Frame(self.menu_frame, bg=col.neutral_white)
        self.menu_wrapper.pack(fill='both', expand=True, pady=(64, 0))