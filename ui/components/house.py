from tkinter import *
from PIL import Image, ImageTk
from config import ColorConfig, FontFamilyConfig

class House(Frame):
    def __init__(self, root_, nom_maison, command=None):
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(root_)
        super().__init__(root_, bg=self.col.primary_white, cursor="hand2")
        super().grid(padx=(0, 48), pady=(0, 48))

        image = Image.open('assets/images/image_house.png')
        image = image.resize((100, 100))
        self.image = ImageTk.PhotoImage(image)

        self.label_image = Label(self, image=self.image, bg=self.col.primary_white, cursor="hand2")
        self.label_image.pack()

        self.label_nom = Label(self, text=nom_maison, bg=self.col.primary_white, fg=self.col.primary_black, font=(self.ff.text_normal, 12, 'bold'), cursor="hand2")
        self.label_nom.pack(pady=8)

        if command:
            self.bind("<Button-1>", lambda e: command())
            self.label_image.bind("<Button-1>", lambda e: command())
            self.label_nom.bind("<Button-1>", lambda e: command())


class Room(Frame):
    def __init__(self, root_, nom_piece, room_, command=None):
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(root_)
        super().__init__(root_, bg=self.col.primary_white, cursor="hand2")
        super().grid(padx=(0, 48), pady=(0, 32))

        IMAGE_ROOM = {
            'CUISINE': 'assets/images/image_kitchen.png',
            'SALON': 'assets/images/image_living_room.png',
            'CHAMBRE': 'assets/images/image_room.png',
            'SALLE DE BAIN': 'assets/images/images_bathroom.png'
        }

        image = Image.open(IMAGE_ROOM[room_])
        image = image.resize((150, 150))
        self.image = ImageTk.PhotoImage(image)

        self.label_image = Label(self, image=self.image, bg=self.col.primary_white, cursor="hand2")
        self.label_image.pack()

        self.label_nom = Label(self, text=nom_piece, bg=self.col.primary_white, fg=self.col.primary_black, font=(self.ff.text_normal, 12, 'bold'), cursor="hand2")
        self.label_nom.pack(pady=8)

        if command:
            self.bind("<Button-1>", lambda e: command())
            self.label_image.bind("<Button-1>", lambda e: command())
            self.label_nom.bind("<Button-1>", lambda e: command())


class Heat:
    def __init__(self, root_, initial_temp=18, command=None, delete_command=None):
        self.root = root_
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self.root)

        self.container = Frame(self.root, bg=self.col.neutral_white)
        self.container.pack(ipadx=16, ipady=16, padx=16, fill='x')

        url = Image.open("assets/icons/icon_heat.png").resize((64, 64))
        heat_image = ImageTk.PhotoImage(image=url)

        self.heat_image = Label(self.container, image=heat_image, bg=self.col.neutral_white)
        self.heat_image.image = heat_image
        self.heat_image.pack(side='left', padx=(16, 32))

        self.range = Scale(
            self.container,
            from_=10, to=30,
            orient='horizontal',
            length=400, tickinterval=5,
            bg=self.col.neutral_white,
            fg=self.col.primary_black,
            troughcolor=self.col.primary_blue,
            relief='flat', bd=0,
            command=lambda val: command(int(val)) if command else None
        )
        self.range.set(initial_temp)
        self.range.pack(side='left', fill='x', expand=True)

        self.del_button = Button(
            self.container,
            text="Supprimer",
            bg=self.col.primary_red,
            fg=self.col.neutral_black,
            font=(self.ff.text_normal, 8, "bold"),
            command=delete_command,
            relief="flat",
            borderwidth=0
        )
        self.del_button.pack(side='left', padx=(24, 0))


class Light:
    def __init__(self, root_, active_=False, row=None, column=None, command=None, delete_command=None):
        self.root = root_
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self.root)

        self.container = Frame(self.root, width=200, height=100, bg=self.col.neutral_white, padx=16, pady=16)
        self.container.grid(padx=(0, 16), pady=(0, 16), row=row, column=column)

        # Lamp layout
        theme = self.col.get_theme()
        url_inactive_path = f"assets/icons/icon_lamp_inactive_{theme}.png"
        url_inactive = Image.open(url_inactive_path).resize((64, 64))
        url_active = Image.open("assets/icons/icon_lamp_active.png").resize((64, 64))

        self.lamp_active = ImageTk.PhotoImage(image=url_active)
        self.lamp_inactive = ImageTk.PhotoImage(image=url_inactive)

        self.lamp = Label(self.container, image=self.lamp_active if active_ else self.lamp_inactive, bg=self.col.neutral_white)
        self.lamp.grid(row=0, rowspan=2, column=0, sticky='nsew')

        def on_toggle(state):
            self.lamp.config(image=self.lamp_active if state else self.lamp_inactive)
            if command:
                command(state)

        self.switcher = ToggleSwitch(self.container, initial_state=active_, command=on_toggle)
        self.switcher.grid(row=0, column=1, padx=(24, 0))

        self.del_button = Button(
            self.container,
            text="Supprimer",
            bg=self.col.primary_red,
            fg=self.col.neutral_black,
            font=(self.ff.text_normal, 8, "bold"),
            command=delete_command,
            relief="flat",
            borderwidth=0
        )
        self.del_button.grid(row=1, column=1, padx=(24, 0))


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

    def update_colors(self):
        col = ColorConfig()
        self.button.config(activebackground=col.neutral_white, bg=col.neutral_white)

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