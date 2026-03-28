from tkinter import *
from PIL import Image, ImageTk # pip install pillow (pour installer la biblioteque des images)

class dashbord:
    def __init__(self,root):
        self.root=root
        self.root.title("DOMOHOUSE SYSTEM")
        self.root.geometry("900x500")
        self.root.configure(bg="#f5f5f5")

        icon =PhotoImage(file=r"C:\Users\HP\Documents\L2  informatique\S4\ing_sys_int\projetIG\tableau_bord\img\house-30.png")
        self.root.iconphoto(True,icon)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=4)
        self.root.grid_rowconfigure(0, weight=1)

         # Création des parties
        self.menu_gauche()
        self.menu_droite()

    def menu_gauche(self):
        icon_title = Image.open(r"C:\Users\HP\Documents\L2  informatique\S4\ing_sys_int\projetIG\tableau_bord\img\house-30.png")
        icon_title = icon_title.resize((20, 20))
        icon_title = ImageTk.PhotoImage(icon_title)

        menu_gauche = Frame(self.root, bg="#e6e6e6", width=200)
        menu_gauche.grid(row=0, column=0, sticky="nsew")
        menu_gauche.grid_propagate(False)

        title = Label(menu_gauche, text="DOMOHOUSE SYSTEM",image=icon_title,compound="left", bg="#e6e6e6",
                         font=("Arial", 12, "bold"),padx=10)
        title.image = icon_title
        title.pack(pady=20)

        houses = ["Maison 01", "Maison 02"]

        for i, house in enumerate(houses):
            color = "#f4c542" if i == 0 else "#d9d9d9"

            btn = Button(menu_gauche, text=house, bg=color, relief="flat",
                            padx=10, pady=10)
            btn.pack(fill="x", padx=20, pady=5)


    def menu_droite(self):
        content = Frame(self.root, bg="#ffffff")
        content.grid(row=0, column=1, sticky="nsew")
        
        title = Label(content, text="Tableau de bord - État de la maison",
                    font=("Arial", 16, "bold"), bg="#ffffff")
        title.pack(pady=20)
        
        title1 = Label(content, text="Récapitulatif de toutes les pièces",
                    font=("Arial", 10), bg="#14E3C7")
        title1.pack(pady=5)

        # Frame du tableau
        table = Frame(content, bg="#ffffff")
        table.pack(padx=10, pady=10, fill="x")

        # Configurer colonnes (IMPORTANT)
        for i in range(3):
            table.grid_columnconfigure(i, weight=1)

        # Données
        data = [
            {"piece": "Salon", "eclairage": "2 ALLUMEES - 2 ETEINTS", "temperature": "22 °C"},
            {"piece": "Cuisine", "eclairage": "4 ETEINTS", "temperature": "16 °C"},
            {"piece": "Chambre", "eclairage": "4 ALLUMEES", "temperature": "N/A"}
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
            lbl = Label(table, text=h, font=("Arial", 10, "bold"),
                        bg="#c0c4ff", borderwidth=1)
            lbl.grid(row=0, column=col, sticky="nsew")

        # Lignes
        for row_index, row in enumerate(data, start=1):
            Label(table, text=row["piece"], bg="#0cd0cd",
                borderwidth=1).grid(row=row_index, column=0, sticky="nsew")

            Label(table, text=row["eclairage"], bg="#13eee0",
                fg=get_color(row["eclairage"]),
                borderwidth=1).grid(row=row_index, column=1, sticky="nsew")

            Label(table, text=row["temperature"], bg="#1be3ea",
                borderwidth=1).grid(row=row_index, column=2, sticky="nsew")


if __name__ =="__main__":
    root = Tk()
    dashbord(root)
    root.mainloop()

