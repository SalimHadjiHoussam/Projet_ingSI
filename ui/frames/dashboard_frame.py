from tkinter import *
from config import ColorConfig, FontFamilyConfig
from ui.components.menu import Menu


class Dashboard(Menu):
    def __init__(self, root_):
        super().__init__(root_)
        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self._root)

        # Boutons maisons dans le menu latéral
        houses = ["Maison 01", "Maison 02", "Maison 03", "Maison 04"]
        for i, house in enumerate(houses):
            color = self.col.primary_white if i != 0 else self.col.primary_yellow
            btn = Button(
                self.menu_wrapper,
                text=house,
                bg=color,
                relief="flat",
                padx=10, pady=10
            )
            btn.pack(fill="x", pady=8)

        self._construire_contenu()

    def _construire_contenu(self):
        # ✅ Rattaché à self.frame, pas à self._root
        content = Frame(self.frame, bg=self.col.primary_white, padx=32)
        content.grid(row=0, column=1, sticky="nsew")

        title = Label(
            content,
            text="Tableau de bord - État de la maison",
            font=(self.ff.text_title, 20, "bold", "underline"),
            bg=self.col.primary_white
        )
        title.pack(pady=20)

        title1 = Label(
            content,
            text="Récapitulatif de toutes les pièces",
            font=(self.ff.text_title, 16, "bold"),
            pady=16,
            bg=self.col.primary_white
        )
        title1.pack()

        # Tableau
        table = Frame(content, bg=self.col.primary_white)
        table.pack(padx=10, pady=10, fill="x")

        for i in range(3):
            table.grid_columnconfigure(i, weight=1)

        data = [
            {"piece": "Salon",   "eclairage": "2 ALLUMEES - 2 ETEINTS", "temperature": "22 °C"},
            {"piece": "Cuisine", "eclairage": "4 ETEINTS",              "temperature": "16 °C"},
            {"piece": "Chambre", "eclairage": "4 ALLUMEES",             "temperature": "N/A"},
            {"piece": "Cuisine", "eclairage": "4 ETEINTS",              "temperature": "16 °C"},
            {"piece": "Chambre", "eclairage": "4 ALLUMEES",             "temperature": "N/A"},
            {"piece": "Salon",   "eclairage": "2 ALLUMEES - 2 ETEINTS", "temperature": "22 °C"},
        ]

        def get_color(text):
            if "ALLUMEES" in text:
                return self.col.primary_green
            elif "ETEINTS" in text:
                return self.col.primary_red
            return self.col.neutral_black

        headers = ["Pièces", "Éclairage", "Température"]
        for col_idx, h in enumerate(headers):
            Label(
                table, text=h,
                font=(self.ff.text_normal, 12, "bold"),
                bg="#99acff", borderwidth=1,
                padx=12, pady=12,
                fg=self.col.neutral_white
            ).grid(row=0, column=col_idx, sticky="nsew")

        for row_index, row in enumerate(data, start=1):
            Label(
                table,
                text=row["piece"],
                bg="#cdd6ff",
                borderwidth=1, pady=8, padx=8,
                font=(self.ff.text_normal, 12)
            ).grid(row=row_index, column=0, sticky="nsew")

            Label(
                table,
                text=row["eclairage"],
                bg="#e3e8ff",
                fg=get_color(row["eclairage"]),
                borderwidth=1, pady=8, padx=8,
                font=(self.ff.text_normal, 12, "bold")
            ).grid(row=row_index, column=1, sticky="nsew")

            Label(
                table,
                text=row["temperature"],
                bg="#e3e8ff",
                borderwidth=1, pady=8, padx=8,
                font=(self.ff.text_normal, 12, "bold")
            ).grid(row=row_index, column=2, sticky="nsew")