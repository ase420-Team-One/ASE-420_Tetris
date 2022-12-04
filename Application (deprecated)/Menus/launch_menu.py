from MainMenu import MainMenu, MainMenuBuilder
from Application.Tetris.Tetris import Tetris


class Launcher:
    def __init__(self):
        self._main_menu = MainMenu(MainMenuBuilder, self._start)

    def launch(self):
        self._construct()

    def _construct(self):
        self._main_menu.construct()
        self._main_menu.display()

    def _start(self):
        self._main_menu.retrieve_vars()
        self._main_menu.destroy()
        # TODO process vars, refactor tetris calls
        Tetris.start()
