from tkinter import ttk, messagebox
from Menu import Menu, MenuBuilder
from TkBuilder import TkBuilder
from typing import Callable, Literal
from Application.Util.WidthHeightPair import WidthHeightPair
from Application.Util.tkToPygameTranslator import translator
from Application.Menus.Variables.ControlsVariable import KeyVar
from Application.Controller.Controls import TkScheme
from tkinter import Event


class MainMenuBuilder(MenuBuilder):
    def __init__(self):
        super().__init__()
        self._styler = ttk.Style(self._root)

    def build_geometry(self, window_dimensions: WidthHeightPair):
        # set the position of the window to the center of the screen
        self._root.geometry(self.build_geometry_string(window_dimensions))
        self._root.resizable(False, False)

    def build_geometry_string(self, window_dimensions: WidthHeightPair):
        # get the screen dimensions
        screen_dimensions = WidthHeightPair(self._root.winfo_screenwidth(), self._root.winfo_screenheight())

        # find the center point
        center_x = int(screen_dimensions.width / 2 - screen_dimensions.width / 2)
        center_y = int(screen_dimensions.height / 2 - screen_dimensions.height / 2)

        # f'{window_dimensions.width}x{window_dimensions.height}+{center_x}+{center_y}'
        self._root.geometry(TkBuilder.build_geometry_string(window_dimensions) + f"+{center_x}+{center_y}")

    def build_entry(self,
                    var_str: Literal["down", "drop", "left", "right", "quit_key", "rotateCounter", "rotatePrimary"],
                    var_val: int, frame: ttk.Frame = None):
        holder = self.build_frame(frame=frame, padding=5)
        self.build_label(holder, var_str)
        control_var = self._variables.get_var(var_str)
        control_var.set_key(value=var_val)
        control_var.set(translator.tk_to_pg_name(var_val))

        entry = ttk.Entry(holder, textvariable=control_var)
        self._styler.configure("TEntry", background=[('focus', 'yellow')])
        entry.bind("<KeyRelease>", self._generate_entry_funct(control_var, holder))
        holder.pack(fill="x", expand=True)
        entry.pack()

    def build_kill_button(self, frame: ttk.Frame, text: str):
        self.build_button(frame, text, self._root.destroy)

    def _generate_entry_funct(self, string_var: KeyVar, holder: ttk.Frame) -> Callable[[Event], None]:
        # generated so control var can be adjusted, and so focus is removed from the entry widget
        def _entry_entered(event: Event):
            entry = string_var.get_key()
            try:
                if event.keycode not in self._variables:
                    entry = event.keycode
                else:
                    raise KeyError()
            except KeyError:
                messagebox.showerror("Invalid Entry", "Please Select a Different Key")
            holder.focus_set()
            string_var.set(translator.tk_to_pg_name(entry))

        return _entry_entered

    def get_vars(self):
        return self._variables

    def destroy(self):
        self._root.destroy()


class MainMenu(Menu):
    def __init__(self, menu_builder: type[MainMenuBuilder],
                 game_start: Callable[[], None]) -> None:
        super().__init__(menu_builder)
        self._game_start = game_start

    def retrieve_vars(self):
        return self._menu.get_vars()

    def construct(self):
        self._menu.set_title("Tetris.py")
        self._menu.build_geometry(WidthHeightPair(width=394, height=500))
        menu_frame = self._construct_menu_frame(outer_padding=15, inner_padding=10)
        self._construct_menu_buttons(menu_frame)
        keys = self._construct_inner_menu(frame=menu_frame)
        self._construct_entries(menu_frame)
        return keys

    def _construct_entries(self, menu_frame: ttk.Frame):
        scheme = TkScheme.default_scheme()
        holder = self._menu.build_frame(menu_frame)

        for key, val in scheme.items():
            self._menu.build_entry(var_str=key, frame=holder, var_val=val)

        holder.pack(side="left")

    def _construct_menu_frame(self, outer_padding: int, inner_padding: int):
        outer_frame = self._menu.build_frame(padding=outer_padding, fill="both", expand=True)
        return self._menu.build_frame(frame=outer_frame, padding=inner_padding, fill="both", relief="solid",
                                      expand=True)

    def _construct_inner_menu(self, frame: ttk.Frame):
        checkbox_labels = ["Polymino", "Sound", "Dark Mode", "Background Flash"]
        combo_values_list = {"Starting Level:": ["None", "Level 1", "Level 2", "Level 3"],
                             "Grid Size:": ["Normal", "Large", "Largish", "Smallish", "Small"],
                             "Speed": ["Normal", "Slowest", "Slower", "Faster", "Fastest"]
                             }
        keys: list[str] = []
        checks = map(lambda text_val: self._menu.build_check_box(frame, text_val), checkbox_labels)
        for label, val in combo_values_list.items():
            keys.append(self._menu.build_labelled_combo_box(frame, val, label))

        for item in list(checks):
            keys.append(item)
        return keys

    def _construct_menu_buttons(self, menu_frame: ttk.Frame):
        bottom_button_frame = self._menu.build_frame(menu_frame, fill="y", side="right")

        button_dict = {"Play": self._game_start}

        for label, command in button_dict.items():
            self._menu.build_button(bottom_button_frame, label, command)

    def destroy(self):
        self._menu.destroy()
