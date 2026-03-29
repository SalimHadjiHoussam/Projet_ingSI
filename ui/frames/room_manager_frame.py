from tkinter import *
from config import ColorConfig, FontFamilyConfig
from ui.components.heating import Heat
from ui.components.menu import Menu
from ui.components.light import Light

class RoomManager(Menu):
    def __init__(self, root_):
        super().__init__(root_)
        self.root = root_

        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self.root)

        self.add_lamp_button = Button(
            self.menu_wrapper,
            text="Ajouter une lampe",
            bg=self.col.primary_green,
            padx = 10, pady = 10,
            font=(self.ff.text_normal, 10, "bold")
        )
        self.add_lamp_button.pack(fill='x', pady=8)

        self.add_heating_button = Button(
            self.menu_wrapper,
            text="Ajouter le chauffage",
            bg=self.col.primary_green,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold")
        )
        self.add_heating_button.pack(fill='x', pady=8)

        self.del_room_button = Button(
            self.menu_wrapper,
            text="Supprimer cette pièce",
            bg=self.col.primary_red,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold")
        )
        self.del_room_button.pack(side='bottom', fill='x', pady=8)

        self.main()

    def main(self):

        main_content = Frame(self.root, bg=self.col.primary_white, pady=32, padx=32)
        main_content.grid(row=0, column=1, sticky="nsew")

        title_text = Label(
            main_content,
            text="Réglages de l’éclairage & de la \ntempérature",
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white
        )
        title_text.pack()


        lighting_wrapper = Frame(main_content, bg=self.col.primary_white)
        lighting_wrapper.pack(fill='both', expand=True, pady=(32, 0))

        text_light = Label(lighting_wrapper, text="Éclairage", bg=self.col.primary_white, font=(self.ff.text_normal, 16, 'bold'))
        text_light.grid(row=0, pady=(0, 16), sticky='w')

        div_light = Frame(lighting_wrapper, bg=self.col.primary_white)
        div_light.grid(row=1)

        light_01 = Light(div_light, row=0, column=0, active_=False)
        light_02 = Light(div_light, row=0, column=1, active_=True)
        light_03 = Light(div_light, row=0, column=2, active_=False)
        light_04 = Light(div_light, row=0, column=3, active_=True)
        light_05 = Light(div_light, row=1, column=0, active_=True)


        heating_wrapper = Frame(main_content, bg=self.col.primary_white)
        heating_wrapper.pack(fill='both', expand=True)

        text_heat = Label(heating_wrapper, text="Température", bg=self.col.primary_white,
                     font=(self.ff.text_normal, 16, 'bold'))
        text_heat.grid(row=0, pady=(0, 16), sticky='w')

        div_heat = Frame(heating_wrapper, bg=self.col.primary_white)
        div_heat.grid(row=1)

        heat = Heat(div_heat)