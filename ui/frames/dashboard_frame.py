from tkinter import *
from config import ColorConfig, FontFamilyConfig
from ui.components.menu import Menu


from controllers.main_controller import fetch_dashboard_data, fetch_houses

class Dashboard(Menu):
    def __init__(self, root_, house_id=None, go_back_callback=None, goto_dashboard=None, goto_home_callback=None):
        super().__init__(root_, go_back_callback=go_back_callback, goto_home_callback=goto_home_callback)
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)
        self.house_id = house_id
        self.goto_dashboard = goto_dashboard

        self._recharger_menu()
        self._construire_contenu()

    def show(self):
        super().show()
        self._recharger_menu()
        self._construire_contenu()

    def _recharger_menu(self):
        for widget in self.menu_wrapper.winfo_children():
            widget.destroy()

        # Liste des maisons dans le menu
        Label(
            self.menu_wrapper,
            text="Mes Maisons",
            font=(self.ff.text_normal, 12, "bold"),
            bg=self.col.neutral_white,
            fg=self.col.primary_blue
        ).pack(pady=(10, 10), fill="x")

        # Bouton "Toutes les maisons"
        Button(
            self.menu_wrapper,
            text="Toutes les maisons",
            font=(self.ff.text_normal, 10),
            bg=self.col.primary_yellow if self.house_id is None else self.col.primary_white,
            fg=self.col.primary_black,
            command=lambda: self.goto_dashboard(None) if self.goto_dashboard else None,
            relief="flat",
            cursor="hand2"
        ).pack(fill="x", pady=2)

        houses = fetch_houses()
        for h_id, h_name in houses:
            is_active = (self.house_id == h_id)
            Button(
                self.menu_wrapper,
                text=h_name,
                font=(self.ff.text_normal, 10),
                bg=self.col.primary_yellow if is_active else self.col.primary_white,
                fg=self.col.primary_black,
                command=lambda id_=h_id: self.goto_dashboard(id_) if self.goto_dashboard else None,
                relief="flat",
                cursor="hand2"
            ).pack(fill="x", pady=2)
    def _construire_contenu(self):
        # On nettoie le contenu précédent dans la frame de contenu
        # Recherche de la frame de contenu (colonne 1)
        for widget in self.frame.grid_slaves(row=0, column=1):
            widget.destroy()

        content = Frame(self.frame, bg=self.col.primary_white, padx=32)
        content.grid(row=0, column=1, sticky="nsew")

        titre_texte = "Tableau de bord - État global" if self.house_id is None else "Récapitulatif de la maison"
        
        title = Label(
            content,
            text=titre_texte,
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white,
            fg=self.col.primary_black
        )
        title.pack(pady=20)

        # Canvas et Scrollbar pour le cas où il y a beaucoup de données
        canvas = Canvas(content, bg=self.col.primary_white, highlightthickness=0)
        scrollbar = Scrollbar(content, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.col.primary_white)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Récupération des données réelles (filtrées si house_id est présent)
        data = fetch_dashboard_data(self.house_id)

        if not data:
            Label(
                scrollable_frame, 
                text="Aucune donnée disponible. Créez des maisons et des pièces d'abord.",
                font=(self.ff.text_normal, 12),
                bg=self.col.primary_white,
                fg=self.col.primary_black
            ).pack(pady=20)
            return

        # Groupement par maison
        houses_data = {}
        for h_name, r_id, r_name, r_type, l_on, l_off, temp in data:
            if h_name not in houses_data:
                houses_data[h_name] = []
            houses_data[h_name].append({
                "piece": r_name,
                "eclairage": f"{l_on} ALLUMEE(S) - {l_off} ETEINTE(S)" if (l_on + l_off) > 0 else "AUCUNE LAMPE",
                "temperature": f"{temp} °C" if temp is not None else "N/A"
            })

        for house_name, rooms in houses_data.items():
            house_section = Frame(scrollable_frame, bg=self.col.primary_white, pady=10)
            house_section.pack(fill="x", expand=True)

            Label(
                house_section,
                text=house_name,
                font=(self.ff.text_title, 16, "bold"),
                bg=self.col.primary_white,
                fg=self.col.primary_blue,
                anchor="w"
            ).pack(fill="x", padx=10)

            table = Frame(house_section, bg=self.col.primary_white)
            table.pack(padx=10, pady=5, fill="x")

            for i in range(3):
                table.grid_columnconfigure(i, weight=1)

            headers = ["Pièces", "Éclairage", "Température"]
            for col_idx, h in enumerate(headers):
                Label(
                    table, text=h,
                    font=(self.ff.text_normal, 11, "bold"),
                    bg="#99acff", borderwidth=1,
                    padx=10, pady=10,
                    fg=self.col.neutral_white
                ).grid(row=0, column=col_idx, sticky="nsew")

            for row_index, row in enumerate(rooms, start=1):
                # Gestion de la couleur pour l'éclairage
                l_color = self.col.neutral_black
                if "AUCUNE LAMPE" in row["eclairage"]:
                    l_color = self.col.neutral_black
                elif "0 ALLUMEE(S)" in row["eclairage"]:
                    l_color = self.col.primary_red
                else:
                    l_color = self.col.primary_green

                # Gestion de la couleur pour la température
                t_color = self.col.neutral_black
                if "°C" in row["temperature"]:
                    try:
                        t_val = float(row["temperature"].replace("°C", "").strip())
                        if t_val < 18:
                            t_color = self.col.primary_blue
                        elif 18 <= t_val <= 24:
                            t_color = self.col.primary_yellow
                        else:
                            t_color = self.col.primary_red
                    except: pass

                Label(
                    table, text=row["piece"],
                    bg="#cdd6ff", borderwidth=1, pady=6, padx=6,
                    font=(self.ff.text_normal, 11),
                    fg=self.col.neutral_black
                ).grid(row=row_index, column=0, sticky="nsew")

                Label(
                    table, text=row["eclairage"],
                    bg="#e3e8ff", fg=l_color,
                    borderwidth=1, pady=6, padx=6,
                    font=(self.ff.text_normal, 11, "bold")
                ).grid(row=row_index, column=1, sticky="nsew")

                Label(
                    table, text=row["temperature"],
                    bg="#e3e8ff", fg=t_color,
                    borderwidth=1, pady=6, padx=6,
                    font=(self.ff.text_normal, 11, "bold")
                ).grid(row=row_index, column=2, sticky="nsew")