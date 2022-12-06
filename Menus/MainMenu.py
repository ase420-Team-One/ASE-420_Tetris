from tkinter import ttk, messagebox
from Menus.Menu import Menu, MenuBuilder
from Menus.TkBuilder import TkBuilder
from Util.WidthHeightPair import WidthHeightPair
from Util.tkToPygameTranslator import translator
from Menus.Variables.ControlsVariable import KeyVar
from Controller.Controls import TkScheme
from tkinter import Event
from PIL import Image, ImageTk
from collections.abc import Callable
from Util.Types import *


class MainMenuBuilder(MenuBuilder):
    def __init__(self):
        super().__init__()
        self._styler = ttk.Style(self._root)

    def build_image(self, dimensions: WidthHeightPair, frame: ttk.Frame = None):
        holder = self._root if frame is None else frame
        image1 = Image.open("assets/img/banner.jpg").resize(dimensions.pair)
        test = ImageTk.PhotoImage(image1)

        label1 = ttk.Label(holder, image=test)
        label1.image = test
        label1.pack()

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
                    var_str: ControlLiteral,
                    var_val: int, frame: ttk.Frame = None):
        holder = self.build_frame(frame=frame, padding=3)
        self.build_label(holder, var_str)

        # the variable key is not returned because it is the same as the list names.
        control_var = self._variables.get_var(var_str)
        control_var.set_key(value=var_val)

        entry = ttk.Entry(holder, textvariable=control_var, width=10)
        self._styler.configure("TEntry", background=[('focus', 'yellow')])
        entry.bind("<KeyRelease>", self._generate_entry_funct(control_var, holder))
        holder.pack(fill="x", expand=True)
        entry.pack(side="right")

    def build_kill_button(self, frame: ttk.Frame, text: str):
        self.build_button(frame, text, self._root.destroy)

    def _generate_entry_funct(self, string_var: KeyVar, holder: ttk.Frame) -> Callable[[Event], None]:
        # generated so control var can be adjusted, and so focus is removed from the entry widget
        def _entry_entered(event: Event):
            entry = string_var.get_key()
            try:
                if not self._variables.contains_value(event.keycode):
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
        self._menu.build_geometry(WidthHeightPair(width=394, height=530))
        menu_frame = self._construct_menu_frame(outer_padding=15, inner_padding=10)
        self._construct_menu_buttons(menu_frame)
        self._construct_entries(menu_frame)
        keys = self._construct_inner_menu(frame=menu_frame)
        return keys

    def _construct_entries(self, menu_frame: ttk.Frame):
        scheme = TkScheme.default_scheme()
        holder = self._menu.build_label_frame(menu_frame, "Controls", padding=3)
        side = self._side_switcher(len(scheme), holder=holder)
        for key, val in scheme.items():
            self._menu.build_entry(var_str=key, frame=side.send(None), var_val=val)

        holder.pack()


    def _construct_menu_frame(self, outer_padding: int, inner_padding: int):
        self._menu.build_image(WidthHeightPair(width=395, height=121))

        outer_frame = self._menu.build_frame(padding=outer_padding, fill="both", expand=True)
        return self._menu.build_frame(frame=outer_frame, padding=inner_padding, fill="both", relief="solid",
                                      expand=True)

    def _construct_inner_menu(self, frame: ttk.Frame):
        holder = self._menu.build_label_frame(frame, "Settings", padding=3)

        checkbox_labels = ["Polymino", "Sound", "Dark Mode"]
        combo_values_list: dict[str, list[str]] = {
            "Starting Level": ["None", "Level 1", "Level 2", "Level 3"],
            "Grid Size": ["Normal", "Large", "Largish", "Smallish", "Small"],
            "Speed": ["Normal", "Slowest", "Slower", "Faster", "Fastest"]
            }

        keys: list[str] = []
        switcher = self._side_switcher(len(checkbox_labels), holder)
        maps = [map(lambda item: self._menu.build_labelled_combo_box(holder, item[1], item[0]), combo_values_list.items()),
                    map(lambda text_val, side_holder: self._menu.build_check_box(side_holder, text_val), checkbox_labels, switcher)]

        for map_var in maps:
            keys.extend(map_var)

        switcher.close()
        return keys

    def _side_switcher(self, limit: int, holder: ttk.Frame):
        holders = [self._menu.build_frame(holder, side="left"), self._menu.build_frame(holder, side="right")]
        total = 0
        while total < limit:
            yield holders[total % 2]
            total += 1

    def _construct_menu_buttons(self, menu_frame: ttk.Frame):
        bottom_button_frame = self._menu.build_frame(menu_frame, fill="y", side="bottom")

        # , "High Scores": self._high_score_window
        button_dict = {"Play": self._game_start}

        for label, command in button_dict.items():
            self._menu.build_button(bottom_button_frame, label, command)

    def destroy(self):
        self._menu.destroy()
