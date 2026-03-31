from tkinter import *
from PIL import ImageTk, Image
from config import ColorConfig, FontFamilyConfig


class Menu:
    """
    Classe de base pour toutes les pages avec menu latéral.
    Chaque page héritant de Menu est encapsulée dans self.frame (le conteneur principal).
    Utiliser show() / hide() pour la navigation.
    """
    def __init__(self, root_, go_back_callback=None, goto_home_callback=None):
        self._root = root_  # la vraie fenêtre Tk
        self.go_back_callback = go_back_callback
        self.goto_home_callback = goto_home_callback

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

        # Bouton Retour
        if self.go_back_callback:
            self.back_btn = Button(
                self.menu_frame,
                text="← Retour",
                command=self.go_back_callback,
                bg=col.neutral_white,
                relief="flat",
                font=(ff.text_normal, 10, "bold"),
                cursor="hand2",
                fg=col.primary_blue,
                activebackground=col.neutral_white,
                activeforeground=col.primary_blue
            )
            self.back_btn.pack(side="bottom", anchor="se", pady=(0, 20), fill="x")

        # Déterminer l'icône selon le thème
        theme = col.get_theme()
        icon_path = "assets/icons/icon_house_light.png" if theme == "sombre" else "assets/icons/icon_house_dark.png"
        
        image = Image.open(fp=icon_path)
        image = ImageTk.PhotoImage(image.resize((32, 32)))

        self.home_wrapper = Frame(self.menu_frame, bg=col.neutral_white)
        self.home_wrapper.pack(anchor="w", fill="x")

        self.home_icon = Button(
            self.home_wrapper,
            image=image,
            bg=col.neutral_white,
            borderwidth=0,
            relief="flat",
            cursor="hand2",
            activebackground=col.neutral_white,
            command=self.goto_home_callback if self.goto_home_callback else None
        )
        self.home_icon.image = image
        self.home_icon.grid(row=0, column=0)

        self.home_text = Label(
            self.home_wrapper,
            text=str.upper("DomoHouse System"),
            font=(ff.text_title, 14, "bold"),
            bg=col.neutral_white,
            padx=8,
            fg=col.primary_black
        )
        self.home_text.grid(row=0, column=1)

        self.menu_wrapper = Frame(self.menu_frame, bg=col.neutral_white)
        self.menu_wrapper.pack(fill="both", expand=True, pady=(64, 0))

    def show(self):
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)
        self._update_menu_colors()

    def _update_menu_colors(self):
        col = ColorConfig()
        ff = FontFamilyConfig(self._root)
        
        self.frame.configure(bg=col.primary_white)
        self.menu_frame.configure(bg=col.neutral_white)
        self.menu_wrapper.configure(bg=col.neutral_white)
        self.home_wrapper.configure(bg=col.neutral_white)
        
        # Mettre à jour l'icône
        theme = col.get_theme()
        icon_path = "assets/icons/icon_house_light.png" if theme == "sombre" else "assets/icons/icon_house_dark.png"
        image = Image.open(fp=icon_path)
        image = ImageTk.PhotoImage(image.resize((32, 32)))
        self.home_icon.configure(image=image, bg=col.neutral_white, activebackground=col.neutral_white)
        self.home_icon.image = image
        
        self.home_text.configure(bg=col.neutral_white, fg=col.primary_black)
        
        if hasattr(self, 'back_btn'):
            self.back_btn.configure(
                bg=col.neutral_white, 
                fg=col.primary_blue, 
                activebackground=col.neutral_white
            )

    def hide(self):
        self.frame.place_forget()