from tkinter import Frame, Label, Scale, Button
from PIL import Image, ImageTk

from config import ColorConfig, FontFamilyConfig


class Heat:
    def __init__(self, root_):
        self.root = root_
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self.root)

        self.container = Frame(self.root, bg=self.col.neutral_white)
        self.container.pack(ipadx=16, ipady=16, padx=16)

        url = Image.open("assets/icons/icon_heat.png").resize((64, 64))
        heat_image = ImageTk.PhotoImage(image=url)

        self.heat_image = Label(self.container, image=heat_image, bg=self.col.neutral_white)
        self.heat_image.image = heat_image
        self.heat_image.pack(side='left', padx=(16, 32))

        self.range = Scale(
            self.container,
            from_=10, to=30,
            orient='horizontal',
            length=550, tickinterval=5,
            bg=self.col.neutral_white,
            troughcolor=self.col.primary_blue,
            relief='flat', bd=0
        )
        self.range.pack(side='left', fill='x')

        self.del_button = Button(
            self.container,
            text="Supprimer",
            bg=self.col.primary_red,
            font=(self.ff.text_normal, 6, "bold")
        )
        self.del_button.pack(side='left', fill='x', padx=(24, 0))