from tkinter import *

from config import ColorConfig


class ToggleSwitch(Frame):
    def __init__(self, parent,
                 on_image_path="assets/icons/on.png",
                 off_image_path="assets/icons/off.png",
                 initial_state=True,
                 command=None,
                 *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        self.is_on = initial_state
        self.command = command

        # Charger images
        self.on_image = PhotoImage(file=on_image_path, width=68, height=30)
        self.off_image = PhotoImage(file=off_image_path, width=68, height=30)

        # Bouton (contenu du Frame)
        self.button = Button(
            self,
            image=self.on_image if self.is_on else self.off_image,
            bd=0,
            highlightthickness=0,
            relief="flat",
            activebackground=ColorConfig().neutral_white,
            bg=ColorConfig().neutral_white,
            command=self.toggle
        )
        self.button.pack()

    def toggle(self):
        self.is_on = not self.is_on

        self.button.config(
            image=self.on_image if self.is_on else self.off_image
        )

        if self.command:
            self.command(self.is_on)

    def get(self):
        return self.is_on

    def set(self, state: bool):
        self.is_on = state
        self.button.config(
            image=self.on_image if self.is_on else self.off_image
        )