from Menus.MainMenu import MainMenu, MainMenuBuilder
from Tetris import Tetris
from Controller.Controls import *
from SpeedControl.speed import speed_dict
from GridControl.grid import grid_dict
from SoundControl.sound import Sound as sound


class Launcher:
    def __init__(self):
        self._main_menu = MainMenu(MainMenuBuilder, self._start)

    def launch(self):
        self._construct()

    def _construct(self):
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
        sound_var = sound(vars["ck_Sound"].get())
        ops = Operators(sound_var)
        control_map = ControlMap(pygame_scheme, ops)


        print(vars)
        
        Tetris().start(
            is_dark_mode = vars["ck_Dark Mode"].get(), 
            grid_user_input= grid_dict[vars["cb_Grid Size"].get()],
            speed_user_input= speed_dict[vars["cb_Speed"].get()], 
            control_map=control_map,
            soundvar = sound_var,
            ops = ops)