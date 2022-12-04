from Themes.colors import Colors


class BackgroundColor(Colors):
    def __init__(self):
        super().__init__()
        self._default = Colors().SECONDARY

    def get_default_background(self):
        return self._default

    def get_flashing_background(self):
        random_num = Colors().random()

        return Colors().select_background_color(random_num)
