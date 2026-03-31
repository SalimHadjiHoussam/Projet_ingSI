from tkinter import *
from tkinter.ttk import Combobox
from config import ColorConfig, FontFamilyConfig
from ui.components.menu import Menu
from ui.components.house import House, Room, Light, Heat


class HousesManager(Menu):
    def __init__(self, root_, goto_dashboard):
        super().__init__(root_)
        self.goto_dashboard = goto_dashboard
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        label_nom = Label(
            self.menu_wrapper,
            anchor="w",
            text="Nom de la maison",
            bg=self.col.neutral_white
        )
        label_nom.pack(pady=(15, 5), fill="x")

        self.champ_nom = Entry(
            self.menu_wrapper,
            bg=self.col.primary_white,
            relief="flat"
        )
        self.champ_nom.pack(pady=5, ipady=5, fill="x")

        self.bouton_ajouter = Button(
            self.menu_wrapper,
            text="Créer",
            font=(self.ff.text_normal, 10, "bold"),
            bg=self.col.primary_green,
            fg=self.col.neutral_black,
            relief="flat"
        )
        self.bouton_ajouter.pack(pady=10, ipadx=20, ipady=5, fill="x")

        self.bouton_dashboard = Button(
            self.menu_wrapper,
            text="Tableau de bord",
            font=(self.ff.text_normal, 10, "bold"),
            bg=self.col.primary_yellow,
            fg=self.col.neutral_black,
            relief="flat",
            command=self.goto_dashboard
        )
        self.bouton_dashboard.pack(pady=5, ipadx=10, ipady=5, fill="x", side="bottom")

        self._construire_contenu()

    def _construire_contenu(self):
        # ✅ Rattaché à self.frame, pas à self._root
        main_content = Frame(self.frame, bg=self.col.primary_white, pady=32, padx=64)
        main_content.grid(row=0, column=1, sticky="nsew")

        title_text = Label(
            main_content,
            text="Créer une maison",
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white
        )
        title_text.pack(pady=(0, 16))

        div = Frame(main_content, bg=self.col.primary_white)
        div.pack(fill="both", expand=True, pady=(32, 0))

        houses = [
            House(div, "Ma maison 1"),
            House(div, "Ma maison 2"),
            House(div, "Ma maison 3"),
            House(div, "Ma maison 4"),
            House(div, "Ma maison 5"),
            House(div, "Ma maison 6"),
            House(div, "Ma maison 7"),
            House(div, "Ma maison 8"),
            House(div, "Ma maison 9"),
            House(div, "Ma maison 10"),
            House(div, "Ma maison 11"),
            House(div, "Ma maison 12"),
            House(div, "Ma maison 13"),
        ]
        i, k = 0, 0
        for h in houses:
            if i > 4: i, k = 0, k + 1
            h.grid(row=k, column=i)
            i += 1


class HouseManager(Menu):
    def __init__(self, root_):
        super().__init__(root_)
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        Label(
            self.menu_wrapper,
            anchor="w",
            text="Choisir une pièce",
            bg=self.col.neutral_white
        ).pack(pady=(10, 5), fill="x")

        self.menu_deroulant = Combobox(
            self.menu_wrapper,
            background=self.col.neutral_white,
            values=["CUISINE", "SALON", "CHAMBRE", "SALLE DE BAIN"],
            state="readonly"
        )
        self.menu_deroulant.pack(pady=5, ipady=6, fill="x")
        self.menu_deroulant.set("CUISINE")

        Label(
            self.menu_wrapper,
            anchor="w",
            text="Nom de la pièce",
            bg=self.col.neutral_white
        ).pack(pady=(15, 5), fill="x")

        self.champ_nom = Entry(
            self.menu_wrapper,
            bg=self.col.primary_white,
            relief="flat"
        )
        self.champ_nom.pack(pady=5, ipady=5, fill="x")

        Button(
            self.menu_wrapper,
            text="Ajouter",
            font=(self.ff.text_normal, 10, "bold"),
            bg=self.col.primary_green,
            fg=self.col.neutral_black,
            relief="flat"
        ).pack(pady=10, ipadx=20, ipady=5, fill="x")

        Button(
            self.menu_wrapper,
            text="Supprimer cette maison",
            font=(self.ff.text_normal, 10, "bold"),
            bg=self.col.primary_red,
            fg=self.col.neutral_black,
            relief="flat"
        ).pack(pady=5, ipadx=10, ipady=5, fill="x", side="bottom")

        self._construire_contenu()

    def _construire_contenu(self):
        main_content = Frame(self.frame, bg=self.col.primary_white, pady=32, padx=64)
        main_content.grid(row=0, column=1, sticky="nsew")

        Label(
            main_content,
            text="Ajouter une pièce",
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white
        ).pack(pady=(0, 16))

        div = Frame(main_content, bg=self.col.primary_white)
        div.pack(fill="both", expand=True, pady=(32, 0))

        rooms = [
            Room(div, "Ma cuisine",       "CUISINE"),
            Room(div, "Mon salon",        "SALON"),
            Room(div, "Ma chambre 1",     "CHAMBRE"),
            Room(div, "Ma chambre 2",     "CHAMBRE"),
            Room(div, "Ma salle de bain", "SALLE DE BAIN"),
        ]
        i, k = 0, 0
        for r in rooms:
            if i > 3: i, k = 0, k+1
            r.grid(row=k, column=i)
            i += 1


class RoomManager(Menu):
    def __init__(self, root_):
        super().__init__(root_)
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        Button(
            self.menu_wrapper,
            text="Ajouter une lampe",
            bg=self.col.primary_green,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold")
        ).pack(fill="x", pady=8)

        Button(
            self.menu_wrapper,
            text="Ajouter le chauffage",
            bg=self.col.primary_green,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold")
        ).pack(fill="x", pady=8)

        Button(
            self.menu_wrapper,
            text="Supprimer cette pièce",
            bg=self.col.primary_red,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold")
        ).pack(side="bottom", fill="x", pady=8)

        self._construire_contenu()

    def _construire_contenu(self):
        main_content = Frame(self.frame, bg=self.col.primary_white, pady=32, padx=32)
        main_content.grid(row=0, column=1, sticky="nsew")

        Label(
            main_content,
            text="Réglages de l'éclairage & de la \ntempérature",
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white
        ).pack()

        lighting_wrapper = Frame(main_content, bg=self.col.primary_white)
        lighting_wrapper.pack(fill="both", expand=True, pady=(32, 0))

        Label(
            lighting_wrapper,
            text="Éclairage",
            bg=self.col.primary_white,
            font=(self.ff.text_normal, 16, "bold")
        ).grid(row=0, pady=(0, 16), sticky="w")

        div_light = Frame(lighting_wrapper, bg=self.col.primary_white)
        div_light.grid(row=1)

        Light(div_light, row=0, column=0, active_=False)
        Light(div_light, row=0, column=1, active_=True)
        Light(div_light, row=0, column=2, active_=False)
        Light(div_light, row=0, column=3, active_=True)
        Light(div_light, row=1, column=0, active_=True)

        heating_wrapper = Frame(main_content, bg=self.col.primary_white)
        heating_wrapper.pack(fill="both", expand=True)

        Label(
            heating_wrapper,
            text="Température",
            bg=self.col.primary_white,
            font=(self.ff.text_normal, 16, "bold")
        ).grid(row=0, pady=(0, 16), sticky="w")

        div_heat = Frame(heating_wrapper, bg=self.col.primary_white)
        div_heat.grid(row=1)

        Heat(div_heat)