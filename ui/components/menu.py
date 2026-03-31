from tkinter import *
from PIL import ImageTk, Image
from config import ColorConfig, FontFamilyConfig


class Menu:
    """
    Classe de base pour toutes les pages avec menu latéral.
    Chaque page héritant de Menu est encapsulée dans self.frame (le conteneur principal).
    Utiliser show() / hide() pour la navigation.
    """
    def __init__(self, root_):
        self._root = root_  # la vraie fenêtre Tk

        col = ColorConfig()
        ff = FontFamilyConfig(self._root)

        # ── Conteneur principal de la page ──────────────────────
        self.frame = Frame(self._root, bg=col.primary_white)

        # Grille interne : colonne 0 = menu, colonne 1 = contenu
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=5)
        self.frame.grid_rowconfigure(0, weight=1)

        # ── Menu latéral ────────────────────────────────────────
        self.menu_frame = Frame(self.frame, width=220, padx=24, pady=32, bg=col.neutral_white)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        image = Image.open(fp="assets/icons/icon_house.png")
        image = ImageTk.PhotoImage(image.resize((32, 32)))

        self.home_wrapper = Frame(self.menu_frame, bg=col.neutral_white)
        self.home_wrapper.pack(anchor="w", fill="x")

        self.home_icon = Label(
            self.home_wrapper,
            image=image,
            bg=col.neutral_white,
            borderwidth=3,
            relief="solid"
        )
        self.home_icon.image = image
        self.home_icon.grid(row=0, column=0)

        self.home_text = Label(
            self.home_wrapper,
            text=str.upper("DomoHouse System"),
            font=(ff.text_title, 18, "bold"),
            bg=col.neutral_white,
            padx=16
        )
        self.home_text.grid(row=0, column=1)

        self.menu_wrapper = Frame(self.menu_frame, bg=col.neutral_white)
        self.menu_wrapper.pack(fill="both", expand=True, pady=(64, 0))

    def show(self):
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)

    def hide(self):
        self.frame.place_forget()