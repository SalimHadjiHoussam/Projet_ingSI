import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Ajouter_pieces(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Domohouse System")
        self.geometry("1000x550")
        self.configure(bg="#dcdcdc")

        self.creer_interface()

    def creer_interface(self):
        menu_gauche = MenuGauche(self)
        menu_gauche.pack(side="left", fill="y")

        contenu = ContenuPrincipal(self)
        contenu.pack(side="right", expand=True, fill="both")


class MenuGauche(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e6e6e6", width=220)
        self.pack_propagate(False)
        self.creer_widgets()

    def creer_widgets(self):
        entete = tk.Frame(self, bg="#e6e6e6")
        entete.pack(pady=10)

        image_maison = Image.open("img/maison.png")
        image_maison = image_maison.resize((25, 25))
        self.icone = ImageTk.PhotoImage(image_maison)

        label_icone = tk.Label(entete, image=self.icone, bg="#e6e6e6")
        label_icone.pack(side="left", padx=5)

        titre = tk.Label(entete, text="DOMOHOUSE SYSTEM",
                         bg="#e6e6e6", font=("Arial", 10, "bold"))
        titre.pack(side="left")

        label_menu = tk.Label(self, text="Choisir une pièce", bg="#e6e6e6")
        label_menu.pack(pady=(10, 5))

        liste_menu = ["CUISINE", "SALON", "CHAMBRE", "SALLE DE BAIN", "TOILETTES"]

        self.menu_deroulant = ttk.Combobox(self, values=liste_menu, state="readonly")
        self.menu_deroulant.pack(pady=5)

        # Valeur par défaut
        self.menu_deroulant.set("CUISINE")

        label_nom = tk.Label(self, text="Nom de la pièce", bg="#e6e6e6")
        label_nom.pack(pady=(15, 5))

        self.champ_nom = tk.Entry(self, bg="#f2f2f2", relief="flat")
        self.champ_nom.insert(0, "Ma Cuis")
        self.champ_nom.pack(pady=5, ipadx=10, ipady=5)

        bouton_ajouter = tk.Button(self, text="Ajouter",
                                   bg="#6ecf4f", fg="black", relief="flat")
        bouton_ajouter.pack(pady=10, ipadx=20, ipady=5)

        bouton_supprimer = tk.Button(self, text="Supprimer cette maison",
                                     bg="#ff3b30", fg="black", relief="flat")
        bouton_supprimer.pack(pady=5, ipadx=10, ipady=5)


class CartePiece(tk.Frame):
    def __init__(self, parent, nom_piece, chemin_image):
        super().__init__(parent, bg="white")

        image = Image.open(chemin_image)
        image = image.resize((100, 100))
        self.image = ImageTk.PhotoImage(image)

        label_image = tk.Label(self, image=self.image, bg="white")
        label_image.pack()

        label_nom = tk.Label(self, text=nom_piece, bg="white")
        label_nom.pack(pady=5)


class ContenuPrincipal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5f5f5")
        self.creer_widgets()

    def creer_widgets(self):
        titre = tk.Label(self, text="Ajouter une pièce",
                         font=("Arial", 16, "bold", "underline"),
                         bg="#f5f5f5")
        titre.pack(pady=20)

        grille = tk.Frame(self, bg="#f5f5f5")
        grille.pack()

        # Liste des pièces
        pieces = [
            ("Ma cuisine", "img/cuisine.png"),
            ("Ma chambre 1", "img/chambre.png"),
            ("Ma chambre 2", "img/chambre.png"),
            ("Mon salon", "img/salon.png"),
        ]

        for i, (nom, image) in enumerate(pieces):
            carte = CartePiece(grille, nom, image)
            carte.grid(row=i // 3, column=i % 3, padx=20, pady=20)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Domohouse System")
        self.geometry("1000x550")
        self.configure(bg="#dcdcdc")

        self.creer_interface()

    def creer_interface(self):
        menu_gauche = MenuGauche(self)
        menu_gauche.pack(side="left", fill="y")

        contenu = ContenuPrincipal(self)
        contenu.pack(side="right", expand=True, fill="both")


if __name__ == "__main__":
    app = Ajouter_pieces()
    app.mainloop()