from Menus.Variables import MenuVariables
from SpeedControl.speed import speed_dict
from GameLevel.Level import Level

class SettingsVariable:
    # There's a better way to do this, but time : )
    def __init__(self, menu_var : MenuVariables):
        self.dark_mode      = menu_var["ck_Dark Mode"].get()
        self.starting_level = Level.level_from_setting(menu_var["cb_Starting Level"].get())
        self.grid_size      = menu_var["cb_Grid Size"].get()
        self.speed          = speed_dict[menu_var["cb_Speed"].get()]
        self.polyminos      = menu_var["ck_Polymino"].get()
        self.sound          = menu_var["ck_Sound"].get()