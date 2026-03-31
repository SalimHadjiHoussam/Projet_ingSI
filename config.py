"""
Module de configuration des couleurs et polices pour DomoHouse.
"""

class ColorConfig:
    _instance = None
    _theme = "clair"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ColorConfig, cls).__new__(cls)
            cls._instance._init_colors()
        return cls._instance

    def _init_colors(self):
        if self._theme == "clair":
            self.primary_red = '#FF3131'
            self.primary_white = '#F4F1EC'
            self.primary_yellow = '#FFC818'
            self.primary_black = '#2D2D2D'
            self.primary_green = '#7ED957'
            self.primary_blue = '#5170FF'
            self.neutral_white = '#FFFFFF'
            self.neutral_black = '#000000'
        else:
            self.primary_red = '#FF3131'
            self.primary_white = '#2D2D2D'
            self.primary_yellow = '#FFC818'
            self.primary_black = '#F4F1EC'
            self.primary_green = '#7ED957'
            self.primary_blue = '#5170FF'
            self.neutral_white = '#0F0000'
            self.neutral_black = '#F4F1EC'

    @classmethod
    def set_theme(cls, theme_name):
        cls._theme = theme_name
        if cls._instance:
            cls._instance._init_colors()

    @classmethod
    def get_theme(cls):
        return cls._theme

    def show_palette(self):
        print(
            f"Theme: {self._theme}\n"
            f"primary_red => {self.primary_red}\nprimary_white => {self.primary_white}\n"
            f"primary_yellow => {self.primary_yellow}\nprimary_black => {self.primary_black}\n"
            f"primary_green => {self.primary_green}\nprimary_blue => {self.primary_blue}\n"
            f"neutral_white => {self.neutral_white}\nneutral_black => {self.neutral_black}"
        )


class FontFamilyConfig:
    def __init__(self, root_):
        self.text_normal = "Open Sans"
        self.text_title = "TT Interphases Pro Mono Trl"
        self.text_lobster = "Lobster Two"