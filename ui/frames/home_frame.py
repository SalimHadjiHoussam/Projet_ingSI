import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from config import ColorConfig, FontFamilyConfig

COULEURS = {
    "clair": {
        "fond": "#F4F1EC",
        "texte": "#2D2D2D",
        "separateur": "#2D2D2D",
        "btn_fond": "#F4F1EC",
        "btn_texte": "#2D2D2D",
        "btn_bordure": "#2D2D2D",
        "sous_titre": "#2D2D2D",
    },
    "sombre": {
        "fond": "#2D2D2D",
        "texte": "#F4F1EC",
        "separateur": "#F4F1EC",
        "btn_fond": "#0F0000",
        "btn_texte": "#0B0B0A",
        "btn_bordure": "#F4F1EC",
        "sous_titre": "#F4F1EC",
    }
}

IMAGE_MAISON = "assets/images/image_hero.png"


class Home:
    def __init__(self, root_, on_enter, go_back_callback=None):
        self._root_tk = root_
        self.root = tk.Frame(root_)
        self.on_enter = on_enter

        self.col = ColorConfig()
        self.ff = FontFamilyConfig(self.root)

        self.police_titre = tkfont.Font(family=self.ff.text_title, size=42, weight="bold")
        self.police_sous = tkfont.Font(family=self.ff.text_title, size=18, weight="bold")
        self.police_entete = tkfont.Font(family=self.ff.text_normal, size=11)
        self.police_btn_ici = tkfont.Font(family=self.ff.text_lobster, size=22, weight="bold", slant="italic")
        self.police_btn_thm = tkfont.Font(family=self.ff.text_normal, size=11)

        self._construire_interface()
        self._appliquer_theme()

    def _construire_interface(self):
        self.root.configure(bg=self.col.primary_white)

        self.frame_haut = tk.Frame(self.root, bg=self.col.primary_white)
        self.frame_haut.pack(fill="x", padx=30, pady=(18, 0))

        self.lbl_auteurs = tk.Label(
            self.frame_haut,
            text="Réalisé par Japhet Koyakosso-esso, Harold Chanwin et Salim Hadji Houssam",
            font=self.police_entete,
            bg=self.col.primary_white, fg=self.col.primary_black
        )
        self.lbl_auteurs.pack(side="left")

        self.btn_theme = tk.Button(
            self.frame_haut,
            text="Dark Theme" if self.col.get_theme() == "clair" else "Light Theme",
            font=self.police_btn_thm,
            bg=self.col.neutral_white,
            fg=self.col.primary_black,
            relief="solid",
            bd=1,
            padx=14, pady=6,
            cursor="hand2",
            command=self._basculer_theme
        )
        self.btn_theme.pack(side="right")

        self.canvas_sep = tk.Canvas(
            self.root, height=1,
            bg=self.col.primary_white, highlightthickness=0
        )
        self.canvas_sep.pack(fill="x", padx=30, pady=(4, 0))
        self.ligne_sep = self.canvas_sep.create_line(
            0, 0, 2000, 0, fill=self.col.primary_black, width=1
        )

        self.frame_centre = tk.Frame(self.root, bg=self.col.primary_white)
        self.frame_centre.pack(expand=True, fill="both", padx=60, pady=30)

        self.frame_gauche = tk.Frame(self.frame_centre, bg=self.col.primary_white)
        self.frame_gauche.pack(side="left", expand=True, fill="both")

        img = Image.open(IMAGE_MAISON)
        img = img.resize((750, 400))
        self.photo_maison = ImageTk.PhotoImage(img)

        self.lbl_image = tk.Label(self.frame_gauche, bg=self.col.primary_white)
        self.lbl_image.pack(anchor="w", padx=(0, 0), pady=10)
        self.lbl_image.configure(image=self.photo_maison)

        self.frame_droite = tk.Frame(self.frame_centre, bg=self.col.primary_white)
        self.frame_droite.pack(side="right", expand=True, fill="both")

        tk.Label(self.frame_droite, bg=self.col.primary_white, height=2).pack()

        self.lbl_titre1 = tk.Label(
            self.frame_droite,
            text="DomoHouse",
            font=self.police_titre,
            bg=self.col.primary_white, fg=self.col.primary_black,
            anchor="e", justify="right"
        )
        self.lbl_titre1.pack(fill="x", padx=20)

        self.lbl_titre2 = tk.Label(
            self.frame_droite,
            text="System",
            font=self.police_titre,
            bg=self.col.primary_white, fg=self.col.primary_black,
            anchor="e", justify="right"
        )
        self.lbl_titre2.pack(fill="x", padx=20)

        tk.Label(self.frame_droite, bg=self.col.primary_white, height=1).pack()

        self.lbl_sous1 = tk.Label(
            self.frame_droite,
            text="La gestion intelligente",
            font=self.police_sous,
            bg=self.col.primary_white, fg=self.col.primary_black,
            anchor="e", justify="right"
        )
        self.lbl_sous1.pack(fill="x", padx=20)

        self.lbl_sous2 = tk.Label(
            self.frame_droite,
            text="de votre maison commence",
            font=self.police_sous,
            bg=self.col.primary_white, fg=self.col.primary_black,
            anchor="e", justify="right"
        )
        self.lbl_sous2.pack(fill="x", padx=20)

        tk.Label(self.frame_droite, bg=self.col.primary_white, height=2).pack()

        # Bouton ICI
        self.frame_btn_ici = tk.Frame(self.frame_droite, bg=self.col.primary_white)
        self.frame_btn_ici.pack(anchor="e", padx=20)

        self.btn_ici = tk.Button(
            self.frame_btn_ici,
            text="ICI",
            font=self.police_btn_ici,
            bg=self.col.neutral_white,
            fg=self.col.primary_black,
            relief="solid",
            bd=2,
            width=8, pady=8,
            cursor="hand2",
            command=self.on_enter
        )
        self.btn_ici.pack()

    def show(self):
        self.root.place(x=0, y=0, relwidth=1, relheight=1)

    def hide(self):
        self.root.place_forget()

    def _basculer_theme(self):
        nouveau_theme = "sombre" if self.col.get_theme() == "clair" else "clair"
        self.col.set_theme(nouveau_theme)
        
        self.btn_theme.configure(text="Light Theme" if nouveau_theme == "sombre" else "Dark Theme")
        
        # Mettre à jour toute l'application
        self._root_tk.configure(bg=self.col.primary_white)
        self._appliquer_theme()

    def _appliquer_theme(self):
        self.root.configure(bg=self.col.primary_white)

        # Barre haute
        self.frame_haut.configure(bg=self.col.primary_white)
        self.lbl_auteurs.configure(bg=self.col.primary_white, fg=self.col.primary_black)
        self.btn_theme.configure(bg=self.col.neutral_white, fg=self.col.primary_black)

        # Séparateur
        self.canvas_sep.configure(bg=self.col.primary_white)
        self.canvas_sep.itemconfig(self.ligne_sep, fill=self.col.primary_black)

        # Zone centrale
        self.frame_centre.configure(bg=self.col.primary_white)
        self.frame_gauche.configure(bg=self.col.primary_white)
        self.lbl_image.configure(bg=self.col.primary_white)
        self.frame_droite.configure(bg=self.col.primary_white)

        for widget in self.frame_droite.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=self.col.primary_white, fg=self.col.primary_black)

        self.frame_btn_ici.configure(bg=self.col.primary_white)
        self.btn_ici.configure(bg=self.col.neutral_white, fg=self.col.primary_black)
