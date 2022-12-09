from Menus.MainMenu import MainMenu, MainMenuBuilder
from Menus.Variables.SettingsVariable import SettingsVariable
from Tetris import Tetris
from Controller.Controls import *
from SoundControl.sound import Sound as sound


class Launcher:
    def __init__(self):
        self._main_menu = MainMenu(MainMenuBuilder, self._start)

    def launch(self):
        self._main_menu.construct()
        self._main_menu.display()

    def _start(self):
        vars = self._main_menu.retrieve_vars()
        self._main_menu.destroy()

        control_vars = [
            vars["down"].get_key(), vars["drop"].get_key(),
            vars["left"].get_key(),vars["right"].get_key(),
            vars["quit_key"].get_key(),vars["rotateCounter"].get_key(),
            vars["rotatePrimary"].get_key()]
        
        zipped_controls = dict(zip(ControlScheme.key_list(), control_vars))
        pygame_scheme = TkScheme.custom(zipped_controls).to_pygame_scheme()
        settings = SettingsVariable(vars)
        sound_var = sound(settings.sound)
        ops = Operators(sound_var)
        control_map = ControlMap(pygame_scheme, ops)
        
        Tetris().start(
            settings = settings, 
            control_map=control_map,
            soundvar = sound_var,
            ops = ops)