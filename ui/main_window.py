from ui.frames.manager_frame import HousesManager, HouseManager, RoomManager
from ui.frames.dashboard_frame import Dashboard
from ui.frames.home_frame import Home
from config import ColorConfig


class MainWindow:
    def __init__(self, root_):
        col = ColorConfig()

        self.root = root_
        self.root.title("DomoHouse System")
        self.root.geometry("1024x600")
        self.root.configure(bg=col.primary_white)

        # Historique de navigation
        self.history = []

        # Home est affiché dès le départ
        self.home = Home(self.root, on_enter=self._aller_creation_maison, go_back_callback=self.go_back)
        self.home.show()

        self.dashboard = None
        self.houses_manager = None
        self.house_manager = None
        self.room_manager = None

        self._page_actuelle = self.home

    def _changer_page(self, nouvelle_page, push_to_history=True):
        if self._page_actuelle == nouvelle_page:
            return

        if self._page_actuelle:
            if push_to_history:
                self.history.append(self._page_actuelle)
            self._page_actuelle.hide()

        nouvelle_page.show()
        self._page_actuelle = nouvelle_page

    def go_back(self):
        """
        Logique de retour hiérarchique : retourne à la frame parente logique.
        """
        if isinstance(self._page_actuelle, RoomManager):
            # De RoomManager -> HouseManager (on tente de retrouver l'ID de la maison via la frame actuelle)
            # Puisque RoomManager n'a pas house_id stocké en attribut public, on se base sur la navigation
            # Mais comme on veut une frame "précédente", on peut utiliser l'historique filtré
            # ou simplement appeler la méthode de navigation vers le parent.
            if self.history:
                # On cherche la dernière frame qui est un HouseManager
                for i in range(len(self.history)-1, -1, -1):
                    if isinstance(self.history[i], HouseManager):
                        target = self.history.pop(i)
                        # On vide ce qui était après
                        self.history = self.history[:i]
                        self._changer_page(target, push_to_history=False)
                        return
            self._aller_creation_maison() # fallback

        elif isinstance(self._page_actuelle, HouseManager):
            # De HouseManager -> HousesManager
            self._aller_creation_maison()

        elif isinstance(self._page_actuelle, HousesManager):
            # De HousesManager -> Home
            self._aller_accueil()

        elif isinstance(self._page_actuelle, Dashboard):
            # De Dashboard -> HousesManager (ou Home si pas de maisons)
            self._aller_creation_maison()

        elif isinstance(self._page_actuelle, Home):
            pass # On est déjà à l'accueil

    def _aller_accueil(self):
        self.home = Home(self.root, on_enter=self._aller_creation_maison, go_back_callback=self.go_back)
        self._changer_page(self.home, push_to_history=False)
        self.history = [] # On réinitialise l'historique quand on revient à l'accueil

    def _aller_dans_dashboard(self, house_id=None):
        self.dashboard = Dashboard(self.root, house_id=house_id, go_back_callback=self.go_back, goto_dashboard=self._aller_dans_dashboard, goto_home_callback=self._aller_creation_maison)
        # On ne veut pas que le dashboard s'ajoute à l'historique de manière répétée s'il s'agit de simples filtres
        # Mais ici on garde la logique actuelle
        self._changer_page(self.dashboard)

    def _aller_creation_maison(self):
        self.houses_manager = HousesManager(
            self.root, 
            goto_dashboard=self._aller_dans_dashboard,
            goto_house_rooms=self._aller_creation_piece,
            go_back_callback=self.go_back,
            goto_home_callback=self._aller_creation_maison
        )
        self.history = [] # On vide l'historique quand on arrive au niveau racine du manager
        self._changer_page(self.houses_manager, push_to_history=False)

    def _aller_creation_piece(self, house_id=None, house_name=None):
        self.house_manager = HouseManager(
            self.root, 
            house_id=house_id, 
            house_name=house_name, 
            goto_room_settings=self._aller_gestion_piece,
            go_back_callback=self.go_back,
            goto_home_callback=self._aller_creation_maison
        )
        self._changer_page(self.house_manager)

    def _aller_gestion_piece(self, room_id=None, room_name=None):
        self.room_manager = RoomManager(self.root, room_id=room_id, room_name=room_name, go_back_callback=self.go_back, goto_home_callback=self._aller_creation_maison)
        self._changer_page(self.room_manager)