import tkinter as tk
from tkinter import font as tkfont, messagebox
from PIL import Image, ImageTk
import os

COULEURS = {
    "sombre": {
        "fond_global":    "#1a1a1a",
        "fond_sidebar":   "#000000",
        "fond_droite":    "#2D2D2D",
        "texte_clair":    "#FFFFFF",
        "texte_sombre":   "#2D2D2D",
        "btn_creer_fond": "#05A915",
        "btn_creer_txt":  "#0B0B0B",
        "btn_tdb_fond":   "#FAC107FF",
        "btn_tdb_txt":    "#FFFFFF",
        "entry_fond":     "#F4F1EC",
        "entry_txt":      "#2D2D2D",
        "label_fond":     "#2D2D2D",
        "logo_bd":        "#FFFFFF",
        "titre_droite":   "#FFFFFF",
        "nom_maison_txt": "#FFFFFF",
    },
    "clair": {
        "fond_global":    "#F4F1EC",
        "fond_sidebar":   "#FFFFFF",
        "fond_droite":    "#E8E4DC",
        "texte_clair":    "#2D2D2D",
        "texte_sombre":   "#2D2D2D",
        "btn_creer_fond": "#07C84E",
        "btn_creer_txt":  "#010101",
        "btn_tdb_fond":   "#FFC818",
        "btn_tdb_txt":    "#080000F7",
        "entry_fond":     "#080500",
        "entry_txt":      "#2D2D2D",
        "label_fond":     "#E8E4DC",
        "logo_bd":        "#2D2D2D",
        "titre_droite":   "#2D2D2D",
        "nom_maison_txt": "#2D2D2D",
    }
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_MAISON_ICONE = os.path.join(BASE_DIR, "Images", "image_house.png")

NB_MAISONS_AFFICHEES = 8   # grille 4×2


class PageCreationMaison:
    def __init__(self, root):
        self.root = root
        self.root.title("DomoHouse System – Créer une maison")
        self.root.geometry("1200x720")
        self.root.resizable(False, False)

        # Données
        self.maisons = [f"Maison {str(i+1).zfill(2)}" for i in range(NB_MAISONS_AFFICHEES)]
        self.theme_actuel = "sombre"

        # Polices
        self.police_logo    = tkfont.Font(family="Arial", size=13, weight="bold")
        self.police_label   = tkfont.Font(family="Arial", size=11)
        self.police_entry   = tkfont.Font(family="Arial", size=13)
        self.police_btn     = tkfont.Font(family="Arial", size=14, weight="bold")
        self.police_titre   = tkfont.Font(family="Arial", size=22, weight="bold",
                                          underline=True)
        self.police_maison  = tkfont.Font(family="Arial", size=11, weight="bold")

        self.photos_maison = []   # garde les références PhotoImage

        self._construire_interface()
        self._appliquer_theme()

    def _construire_interface(self):
        self.frame_sidebar = tk.Frame(self.root, width=340)
        self.frame_sidebar.pack(side="left", fill="y")
        self.frame_sidebar.pack_propagate(False)

        self.frame_logo = tk.Frame(self.frame_sidebar, bd=2, relief="solid",
                                   padx=10, pady=8)
        self.frame_logo.pack(padx=24, pady=(28, 0), anchor="w")

        self.lbl_logo_icone = tk.Label(self.frame_logo, text="⌂",
                                       font=tkfont.Font(size=18, weight="bold"))
        self.lbl_logo_icone.pack(side="left", padx=(0, 8))

        self.lbl_logo_texte = tk.Label(self.frame_logo, text="DOMOHOUSE SYSTEM",
                                       font=self.police_logo)
        self.lbl_logo_texte.pack(side="left")

        tk.Frame(self.frame_sidebar, height=1, bg="#555").pack(
            fill="x", padx=0, pady=(20, 0)
        )

        self.lbl_nom = tk.Label(self.frame_sidebar, text="Nom de la maison",
                                font=self.police_label)
        self.lbl_nom.pack(anchor="w", padx=24, pady=(28, 6))

        self.var_nom = tk.StringVar()
        self.entry_nom = tk.Entry(
            self.frame_sidebar,
            textvariable=self.var_nom,
            font=self.police_entry,
            relief="flat",
            bd=0
        )
        self.entry_nom.pack(fill="x", padx=24, ipady=12)

        self.sep_entry = tk.Frame(self.frame_sidebar, height=2)
        self.sep_entry.pack(fill="x", padx=24)

        self.btn_creer = tk.Button(
            self.frame_sidebar,
            text="Créer",
            font=self.police_btn,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self._creer_maison
        )
        self.btn_creer.pack(fill="x", padx=24, pady=(20, 0), ipady=14)

        self.spacer = tk.Frame(self.frame_sidebar)
        self.spacer.pack(expand=True, fill="both")

        self.btn_tdb = tk.Button(
            self.frame_sidebar,
            text="Tableau de bord",
            font=self.police_btn,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self._aller_tableau_de_bord
        )
        self.btn_tdb.pack(fill="x", padx=24, pady=(0, 28), ipady=14)

        self.frame_droite = tk.Frame(self.root)
        self.frame_droite.pack(side="right", expand=True, fill="both")

        self.lbl_titre = tk.Label(
            self.frame_droite,
            text="Créer une maison",
            font=self.police_titre
        )
        self.lbl_titre.pack(pady=(40, 20))

        # Grille
        self.frame_grille = tk.Frame(self.frame_droite)
        self.frame_grille.pack(expand=True)

        self._construire_grille()

    def _construire_grille(self):
      
        for w in self.frame_grille.winfo_children():
            w.destroy()
        self.photos_maison = []

        try:
            img_base = Image.open(IMAGE_MAISON_ICONE)
            img_base = img_base.resize((110, 100), Image.LANCZOS)
        except Exception:
            img_base = None

        colonnes = 4
        for i, nom in enumerate(self.maisons):
            ligne  = i // colonnes
            colonne = i % colonnes

            frame_maison = tk.Frame(self.frame_grille,
                                    bg=COULEURS[self.theme_actuel]["fond_droite"])
            frame_maison.grid(row=ligne, column=colonne, padx=22, pady=14)

            if img_base:
                photo = ImageTk.PhotoImage(img_base)
                self.photos_maison.append(photo)
                lbl_img = tk.Label(frame_maison, image=photo,
                                   bg=COULEURS[self.theme_actuel]["fond_droite"],
                                   cursor="hand2")
                lbl_img.pack()
                lbl_img.bind("<Button-1>", lambda e, n=nom: self._ouvrir_maison(n))
            else:
                tk.Label(frame_maison, text="🏠", font=("Arial", 40),
                         bg=COULEURS[self.theme_actuel]["fond_droite"]).pack()

            lbl_nom = tk.Label(frame_maison, text=nom,
                               font=self.police_maison,
                               fg=COULEURS[self.theme_actuel]["nom_maison_txt"],
                               bg=COULEURS[self.theme_actuel]["fond_droite"])
            lbl_nom.pack(pady=(6, 0))

    def _creer_maison(self):
        nom = self.var_nom.get().strip()
        if not nom:
            messagebox.showwarning("Attention", "Veuillez saisir un nom de maison.")
            return
        nouveau_nom = nom
        if nouveau_nom in self.maisons:
            messagebox.showinfo("Info", f"La maison « {nouveau_nom} » existe déjà.")
            return
        self.maisons.append(nouveau_nom)
        self.var_nom.set("")
        self._construire_grille()
        self._appliquer_theme()

    def _aller_tableau_de_bord(self):
        messagebox.showinfo("Navigation", "Redirection vers le Tableau de bord…\n(fonctionnalité à implémenter par l'équipe)")

    def _ouvrir_maison(self, nom):
        messagebox.showinfo("Maison sélectionnée", f"Ouverture de : {nom}")

    def _appliquer_theme(self):
        c = COULEURS[self.theme_actuel]

        self.root.configure(bg=c["fond_global"])

        self.frame_sidebar.configure(bg=c["fond_sidebar"])
        self.frame_logo.configure(bg=c["fond_sidebar"],
                                  highlightbackground=c["logo_bd"])
        self.lbl_logo_icone.configure(bg=c["fond_sidebar"], fg=c["texte_clair"])
        self.lbl_logo_texte.configure(bg=c["fond_sidebar"], fg=c["texte_clair"])
        self.lbl_nom.configure(bg=c["fond_sidebar"], fg=c["texte_clair"])
        self.entry_nom.configure(bg=c["entry_fond"], fg=c["entry_txt"],
                                 insertbackground=c["entry_txt"])
        self.sep_entry.configure(bg=c["texte_clair"])
        self.btn_creer.configure(bg=c["btn_creer_fond"], fg=c["btn_creer_txt"])
        self.spacer.configure(bg=c["fond_sidebar"])
        self.btn_tdb.configure(bg=c["btn_tdb_fond"], fg=c["btn_tdb_txt"])

        self.frame_droite.configure(bg=c["fond_droite"])
        self.lbl_titre.configure(bg=c["fond_droite"], fg=c["titre_droite"])
        self.frame_grille.configure(bg=c["fond_droite"])

        self._construire_grille()

if __name__ == "__main__":
    root = tk.Tk()
    app = PageCreationMaison(root)
    root.mainloop()
