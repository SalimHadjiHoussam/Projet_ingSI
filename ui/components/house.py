from tkinter import *
from PIL import Image, ImageTk
from config import ColorConfig, FontFamilyConfig

class House(Frame):
    def __init__(self, root_, nom_maison):
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(root_)
        super().__init__(root_, bg=self.col.primary_white)
        super().grid(padx=(0, 48), pady=(0, 48))

        image = Image.open('assets/images/image_house.png')
        image = image.resize((100, 100))
        self.image = ImageTk.PhotoImage(image)

        label_image = Label(self, image=self.image, bg=self.col.primary_white)
        label_image.pack()

        label_nom = Label(self, text=nom_maison, bg=self.col.primary_white, font=(self.ff.text_normal, 12, 'bold'))
        label_nom.pack(pady=8)


class Room(Frame):
    def __init__(self, root_, nom_piece, room_):
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(root_)
        super().__init__(root_, bg=self.col.primary_white)
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

        label_image = Label(self, image=self.image, bg=self.col.primary_white)
        label_image.pack()

        label_nom = Label(self, text=nom_piece, bg=self.col.primary_white, font=(self.ff.text_normal, 12, 'bold'))
        label_nom.pack(pady=8)


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