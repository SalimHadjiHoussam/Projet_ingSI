from tkinter import *
from config import ColorConfig
from ui.components.menu import Menu

class Dashboard(Menu):
    def __init__(self, root_):
        super().__init__(root_)
        self.root = root_
        self.col = ColorConfig()

        # Création des parties
        self.dashboard_menu()
        self.dashboard_main()

    def dashboard_menu(self):

        houses = ["Maison 01", "Maison 02", "Maison 03", "Maison 04"]

        for i, house in enumerate(houses):
            color = "#f4c542" if i == 0 else "#d9d9d9"

            btn = Button(
                self.menu_wrapper,
                text=house, bg=color,
                relief="flat",
                padx=10, pady=10
            )
            btn.pack(fill="x", pady=8)

    def dashboard_main(self):
        content = Frame(self.root, bg=self.col.primary_white, padx=32)
        content.grid(row=0, column=1, sticky="nsew")

        title = Label(
            content,
            text="Tableau de bord - État de la maison",
            font=("Arial", 16, "bold"),
            bg=self.col.primary_white
        )
        title.pack(pady=20)

        title1 = Label(
            content,
            text="Récapitulatif de toutes les pièces",
            font=("Arial", 10),
            bg="#14E3C7"
        )
        title1.pack(pady=5)

        # Frame du tableau
        table = Frame(content, bg=self.col.primary_white)
        table.pack(padx=10, pady=10, fill="x")

        # Configurer colonnes (IMPORTANT)
        for i in range(3):
            table.grid_columnconfigure(i, weight=1)

        # Données
        data = [
            {"piece": "Salon", "eclairage": "2 ALLUMEES - 2 ETEINTS", "temperature": "22 °C"},
            {"piece": "Cuisine", "eclairage": "4 ETEINTS", "temperature": "16 °C"},
            {"piece": "Chambre", "eclairage": "4 ALLUMEES", "temperature": "N/A"},
            {"piece": "Cuisine", "eclairage": "4 ETEINTS", "temperature": "16 °C"},
            {"piece": "Chambre", "eclairage": "4 ALLUMEES", "temperature": "N/A"},
            {"piece": "Salon", "eclairage": "2 ALLUMEES - 2 ETEINTS", "temperature": "22 °C"}
        ]

        # Couleurs
        def get_color(text):
            if "ALLUMEES" in text:
                return "green"
            elif "ETEINTS" in text:
                return "red"
            return "black"

        # Entêtes
        headers = ["Pièces", "Éclairage", "Température"]
        for col, h in enumerate(headers):
            lbl = Label(
                table,
                text=h,
                font=("Arial", 10, "bold"),
                bg="#c0c4ff", borderwidth=1
            )
            lbl.grid(row=0, column=col, sticky="nsew")

        # Lignes
        for row_index, row in enumerate(data, start=1):
            Label(
                table,
                text=row["piece"],
                bg="#0cd0cd",
                borderwidth=1
            ).grid(row=row_index, column=0, sticky="nsew")

            Label(
                table,
                text=row["eclairage"],
                bg="#13eee0",
                fg=get_color(row["eclairage"]),
                borderwidth=1
            ).grid(row=row_index, column=1, sticky="nsew")

            Label(
                table,
                text=row["temperature"],
                bg="#1be3ea",
                borderwidth=1
            ).grid(row=row_index, column=2, sticky="nsew")