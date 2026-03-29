from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
from config import ColorConfig, FontFamilyConfig
from ui.components.switch_button import ToggleSwitch


class Light:
    def __init__(self, root_, active_ :bool=False, row=None, column=None, columnspan=None, rowspan=None):
        self.root = root_
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self.root)

        self.container = Frame(self.root, width=200, height=100, bg=self.col.neutral_white, padx=16, pady=16)
        self.container.grid(padx=(0, 16), pady=(0, 16), row=row, column=column, rowspan=rowspan, columnspan=columnspan)


        # Lamp layout
        url_inactive, url_active = Image.open("assets/icons/icon_lamp_inactive.png"), Image.open(
            "assets/icons/icon_lamp_active.png")
        url_inactive, url_active = url_inactive.resize((64, 64)), url_active.resize((64, 64))

        lamp_active = ImageTk.PhotoImage(image=url_active)
        lamp_inactive = ImageTk.PhotoImage(image=url_inactive)

        self.lamp = Label(self.container, image=lamp_active if active_ else lamp_inactive, bg=self.col.neutral_white)
        self.lamp.image = lamp_active if active_ else lamp_inactive
        self.lamp.grid(row=0, rowspan=2, column=0, sticky='nsew')

        self.switcher = ToggleSwitch(self.container, initial_state=active_)
        self.switcher.grid(row=0, column=1, padx=(24, 0))

        self.del_button = Button(
            self.container,
            text="Supprimer",
            bg=self.col.primary_red,
            font=(self.ff.text_normal, 6, "bold")
        )
        self.del_button.grid(row=1, column=1, padx=(24, 0))

