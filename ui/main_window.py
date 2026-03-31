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

        # Home est affiché dès le départ
        self.home = Home(self.root, on_enter=self._aller_creation_maison)
        self.home.show()

        self.dashboard = None
        self.houses_manager = None
        self.house_manager = None
        self.room_manager = None

        self._page_actuelle = self.home

    def _changer_page(self, nouvelle_page):
        if self._page_actuelle:
            self._page_actuelle.hide()
        nouvelle_page.show()
        self._page_actuelle = nouvelle_page

    def _aller_dans_dashboard(self):
        if not self.dashboard:
            self.dashboard = Dashboard(self.root)
        self._changer_page(self.dashboard)

    def _aller_creation_maison(self):
        if not self.houses_manager:
            self.houses_manager = HousesManager(self.root, goto_dashboard=self._aller_dans_dashboard)
        self._changer_page(self.houses_manager)

    def _aller_creation_piece(self):
        if not self.house_manager:
            self.house_manager = HouseManager(self.root)
        self._changer_page(self.house_manager)

    def _aller_gestion_piece(self):
        if not self.room_manager:
            self.room_manager = RoomManager(self.root)
        self._changer_page(self.room_manager)