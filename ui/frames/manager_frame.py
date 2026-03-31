from tkinter import *
from tkinter.ttk import Combobox
from config import ColorConfig, FontFamilyConfig
from controllers.main_controller import (
    create_house, fetch_houses, remove_house, 
    create_room, fetch_rooms, remove_room,
    create_light, fetch_lights, modify_light_state, remove_light,
    create_heating, fetch_heating, modify_heating_temperature, remove_heating
)
from ui.components.menu import Menu
from ui.components.house import House, Room, Light, Heat


class HousesManager(Menu):
    def __init__(self, root_, goto_dashboard, goto_house_rooms, go_back_callback=None, goto_home_callback=None):
        super().__init__(root_, go_back_callback=go_back_callback, goto_home_callback=goto_home_callback)
        self.goto_dashboard = goto_dashboard
        self.goto_house_rooms = goto_house_rooms
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        self.houses = []

        self.label_nom_menu = Label(
            self.menu_wrapper,
            anchor="w",
            text="Nom de la maison",
            bg=self.col.neutral_white,
            fg=self.col.primary_black
        )
        self.label_nom_menu.pack(pady=(15, 5), fill="x")

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
            relief="flat",
            command=self._ajouter_maison
        )
        self.bouton_ajouter.pack(pady=10, ipadx=20, ipady=5, fill="x")

        self.bouton_dashboard = Button(
            self.menu_wrapper,
            text="Tableau de bord",
            font=(self.ff.text_normal, 10, "bold"),
            bg=self.col.primary_yellow,
            fg=self.col.neutral_black,
            relief="flat",
            command=lambda: self.goto_dashboard()
        )
        self.bouton_dashboard.pack(pady=5, ipadx=10, ipady=5, fill="x", side="bottom")

        self._construire_contenu()
        self._charger_maisons()

    def _ajouter_maison(self):
        nom = self.champ_nom.get()
        if create_house(nom):
            self.champ_nom.delete(0, END)
            self._charger_maisons()

    def _charger_maisons(self):
        # On ré-initialise la config couleur au cas où le thème a changé
        self.col = ColorConfig()
        
        # Nettoyer l'affichage actuel
        for widget in self.div.winfo_children():
            widget.destroy()
        self.houses = []

        # Récupérer les maisons depuis la base de données via le contrôleur
        data = fetch_houses()
        for id_maison, nom in data:
            # On passe une fonction qui appelle goto_house_rooms avec les infos de la maison
            h = House(self.div, nom, command=lambda m_id=id_maison, m_nom=nom: self.goto_house_rooms(m_id, m_nom))
            self.houses.append(h)

        # Afficher les maisons dans la grille
        i, k = 0, 0
        for h in self.houses:
            if i > 4:
                i, k = 0, k + 1
            h.grid(row=k, column=i)
            i += 1

    def show(self):
        super().show()
        self._charger_maisons()
        # Mettre à jour les couleurs des titres et labels
        self.title_label.configure(bg=self.col.primary_white, fg=self.col.primary_black)
        self.label_nom_menu.configure(bg=self.col.neutral_white, fg=self.col.primary_black)

    def _construire_contenu(self):
        # ✅ Rattaché à self.frame, pas à self._root
        main_content = Frame(self.frame, bg=self.col.primary_white, pady=32, padx=64)
        main_content.grid(row=0, column=1, sticky="nsew")

        self.title_label = Label(
            main_content,
            text="Créer une maison",
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white,
            fg=self.col.primary_black
        )
        self.title_label.pack(pady=(0, 16))

        self.div = Frame(main_content, bg=self.col.primary_white)
        self.div.pack(fill="both", expand=True, pady=(32, 0))

class HouseManager(Menu):
    def __init__(self, root_, house_id=None, house_name=None, goto_room_settings=None, go_back_callback=None, goto_home_callback=None):
        super().__init__(root_, go_back_callback=go_back_callback, goto_home_callback=goto_home_callback)
        self.house_id = house_id
        self.house_name = house_name
        self.goto_room_settings = goto_room_settings
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        self.label_choisir = Label(
            self.menu_wrapper,
            anchor="w",
            text="Choisir une pièce",
            bg=self.col.neutral_white,
            fg=self.col.primary_black
        )
        self.label_choisir.pack(pady=(10, 5), fill="x")

        self.menu_deroulant = Combobox(
            self.menu_wrapper,
            background=self.col.neutral_white,
            values=["CUISINE", "SALON", "CHAMBRE", "SALLE DE BAIN"],
            state="readonly"
        )
        self.menu_deroulant.pack(pady=5, ipady=6, fill="x")
        self.menu_deroulant.set("CUISINE")

        self.label_nom_p_menu = Label(
            self.menu_wrapper,
            anchor="w",
            text="Nom de la pièce",
            bg=self.col.neutral_white,
            fg=self.col.primary_black
        )
        self.label_nom_p_menu.pack(pady=(15, 5), fill="x")

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
            relief="flat",
            command=self._ajouter_piece
        ).pack(pady=10, ipadx=20, ipady=5, fill="x")

        Button(
            self.menu_wrapper,
            text="Supprimer cette maison",
            font=(self.ff.text_normal, 10, "bold"),
            bg=self.col.primary_red,
            fg=self.col.neutral_black,
            relief="flat",
            command=self._supprimer_maison
        ).pack(pady=5, ipadx=10, ipady=5, fill="x", side="bottom")

        self._construire_contenu()
        self._charger_pieces()

    def _ajouter_piece(self):
        nom = self.champ_nom.get()
        type_p = self.menu_deroulant.get()
        if self.house_id and create_room(self.house_id, nom, type_p):
            self.champ_nom.delete(0, END)
            self._charger_pieces()

    def _supprimer_maison(self):
        if self.house_id:
            remove_house(self.house_id)
            if self.go_back_callback:
                self.go_back_callback()

    def _charger_pieces(self):
        self.col = ColorConfig()
        for widget in self.div.winfo_children():
            widget.destroy()

        if not self.house_id:
            return

        data = fetch_rooms(self.house_id)
        i, k = 0, 0
        for id_room, nom, type_p in data:
            r = Room(self.div, nom, type_p, command=lambda r_id=id_room, r_nom=nom: self.goto_room_settings(r_id, r_nom))
            if i > 3: i, k = 0, k+1
            r.grid(row=k, column=i)
            i += 1

    def show(self):
        super().show()
        self._charger_pieces()
        # Mettre à jour les couleurs
        self.title_label.configure(bg=self.col.primary_white, fg=self.col.primary_black)
        self.label_choisir.configure(bg=self.col.neutral_white, fg=self.col.primary_black)
        self.label_nom_p_menu.configure(bg=self.col.neutral_white, fg=self.col.primary_black)

    def _construire_contenu(self):
        main_content = Frame(self.frame, bg=self.col.primary_white, pady=32, padx=64)
        main_content.grid(row=0, column=1, sticky="nsew")

        title_text = f"Ajouter une pièce à {self.house_name}" if self.house_name else "Ajouter une pièce"
        self.title_label = Label(
            main_content,
            text=title_text,
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white,
            fg=self.col.primary_black
        )
        self.title_label.pack(pady=(0, 16))

        self.div = Frame(main_content, bg=self.col.primary_white)
        self.div.pack(fill="both", expand=True, pady=(32, 0))


class RoomManager(Menu):
    def __init__(self, root_, room_id=None, room_name=None, go_back_callback=None, goto_home_callback=None):
        super().__init__(root_, go_back_callback=go_back_callback, goto_home_callback=goto_home_callback)
        self.room_id = room_id
        self.room_name = room_name
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        Button(
            self.menu_wrapper,
            text="Ajouter une lampe",
            bg=self.col.primary_green,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold"),
            command=self._ajouter_lampe
        ).pack(fill="x", pady=8)

        Button(
            self.menu_wrapper,
            text="Ajouter le chauffage",
            bg=self.col.primary_green,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold"),
            command=self._ajouter_chauffage
        ).pack(fill="x", pady=8)

        Button(
            self.menu_wrapper,
            text="Supprimer cette pièce",
            bg=self.col.primary_red,
            padx=10, pady=10,
            font=(self.ff.text_normal, 10, "bold"),
            command=self._supprimer_piece
        ).pack(side="bottom", fill="x", pady=8)

        self._construire_contenu()
        self._charger_equipements()

    def _ajouter_lampe(self):
        if self.room_id:
            create_light(self.room_id)
            self._charger_equipements()

    def _ajouter_chauffage(self):
        if self.room_id:
            create_heating(self.room_id)
            self._charger_equipements()

    def _supprimer_piece(self):
        if self.room_id:
            remove_room(self.room_id)
            if self.go_back_callback:
                self.go_back_callback()

    def _charger_equipements(self):
        self.col = ColorConfig()
        # Nettoyer
        for widget in self.div_light.winfo_children():
            widget.destroy()
        for widget in self.div_heat.winfo_children():
            widget.destroy()

        if not self.room_id:
            return

        # Lampes
        lights = fetch_lights(self.room_id)
        i, k = 0, 0
        for l_id, is_on in lights:
            if i > 3:
                i, k = 0, k+1
            l = Light(
                self.div_light, 
                active_=bool(is_on), 
                row=k, column=i,
                command=lambda state, id_l=l_id: modify_light_state(id_l, state),
                delete_command=lambda id_l=l_id: self._supprimer_lampe(id_l)
            )
            l.switcher.update_colors()
            i += 1

        # Chauffage
        heat = fetch_heating(self.room_id)
        if heat:
            h_id, temp = heat
            Heat(
                self.div_heat, 
                initial_temp=temp,
                command=lambda t, id_h=h_id: modify_heating_temperature(id_h, t),
                delete_command=lambda id_h=h_id: self._supprimer_chauffage(id_h)
            )

    def show(self):
        super().show()
        self._charger_equipements()
        # Mettre à jour les couleurs
        self.title_label.configure(bg=self.col.primary_white, fg=self.col.primary_black)
        self.subtitle_light.configure(bg=self.col.primary_white, fg=self.col.primary_black)
        self.subtitle_heat.configure(bg=self.col.primary_white, fg=self.col.primary_black)

    def _supprimer_lampe(self, light_id):
        remove_light(light_id)
        self._charger_equipements()

    def _supprimer_chauffage(self, heat_id):
        remove_heating(heat_id)
        self._charger_equipements()

    def _construire_contenu(self):
        main_content = Frame(self.frame, bg=self.col.primary_white, pady=32, padx=32)
        main_content.grid(row=0, column=1, sticky="nsew")

        title_text = f"Réglages de {self.room_name}" if self.room_name else "Réglages de la pièce"
        self.title_label = Label(
            main_content,
            text=title_text,
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white,
            fg=self.col.primary_black
        )
        self.title_label.pack()

        self.lighting_wrapper = Frame(main_content, bg=self.col.primary_white)
        self.lighting_wrapper.pack(fill="both", expand=True, pady=(32, 0))

        self.subtitle_light = Label(
            self.lighting_wrapper,
            text="Éclairage",
            bg=self.col.primary_white,
            fg=self.col.primary_black,
            font=(self.ff.text_normal, 16, "bold")
        )
        self.subtitle_light.grid(row=0, pady=(0, 16), sticky="w")

        self.div_light = Frame(self.lighting_wrapper, bg=self.col.primary_white)
        self.div_light.grid(row=1)

        self.heating_wrapper = Frame(main_content, bg=self.col.primary_white)
        self.heating_wrapper.pack(fill="both", expand=True)

        self.subtitle_heat = Label(
            self.heating_wrapper,
            text="Température",
            bg=self.col.primary_white,
            fg=self.col.primary_black,
            font=(self.ff.text_normal, 16, "bold")
        )
        self.subtitle_heat.grid(row=0, pady=(0, 16), sticky="w")

        self.div_heat = Frame(self.heating_wrapper, bg=self.col.primary_white)
        self.div_heat.grid(row=1)