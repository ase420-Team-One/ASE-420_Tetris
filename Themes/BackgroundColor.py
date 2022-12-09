from Themes.colors import Colors


class BackgroundColor(Colors):
    def __init__(self, is_dark_mode: bool):
        super().__init__(is_dark_mode=is_dark_mode)
        self._default = self.PRIMARY
    
    def get_default_background(self):
        return self._default

    def get_flashing_background(self):
        random_num = Colors().random()

        return self.select_background_color(random_num)
