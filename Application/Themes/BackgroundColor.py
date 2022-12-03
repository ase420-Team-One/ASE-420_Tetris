from Application.Themes.colors import Colors


class BackgroundColor(Colors):
    def __init__(self):
        super().__init__()
        self._default = Colors().SECONDARY

    def get_default_background(self):
        return self._default

    def get_flashing_background(self, current_mino):
        mino_color = current_mino.get_mino_color()
        random_num = Colors().random()

        return Colors().select_background_color(mino_color+1)
