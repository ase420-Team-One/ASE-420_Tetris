from TkBuilder import TkBuilder
from tkinter import ttk
import tkinter as tk
from copy import deepcopy
from typing import List, Literal
from Application.Menus.Variables.MainMenuVariables import MainMenuVariables


class MenuBuilder(TkBuilder):
    def __init__(self):
        super().__init__()
        self._variables = MainMenuVariables()

    def build_check_box(self, frame: ttk.Frame, text: str):
        holder: ttk.Frame | tk.Tk = self._root if frame is None else frame
        ck_var = tk.BooleanVar(value=False)
        check_box = ttk.Checkbutton(holder, text=text, variable=ck_var)
        check_box.pack()
        check_box.invoke()
        check_box.invoke()
        # combo_i, combo_ii, etc emulates numeration
        return self._variables.add("ck_i", ck_var)

    def build_combo_box(self, frame: ttk.Frame, values: List[str],
                        side: Literal["left", "right", "top", "bottom"] = "left", label: str = ""):
        holder = self._root if frame is None else frame
        value_list = deepcopy(values)
        cb_var = tk.StringVar(value=value_list[0])
        combo_box = ttk.Combobox(holder, textvariable=cb_var, values=value_list)
        combo_box.set(value_list[0])
        combo_box.pack(side=side)
        # combo_i, combo_ii, etc
        return self._variables.add("cb_" + label, cb_var)

    def build_labelled_combo_box(self, frame: ttk.Frame, values: List[str], label: str =""):
        outer_frame: ttk.Frame | tk.Tk = self._root if frame is None else frame
        holder = self.build_frame(outer_frame)
        self.build_label(holder, text=label)
        return self.build_combo_box(holder, values, label=label)


class Menu:
    def __init__(self, menu_builder: type[TkBuilder]) -> None:
        self._menu = menu_builder()
        pass

    def construct(self) -> List[str] | None:
        """builds the window, returns the keys"""
        pass

    def display(self):
        self._menu.display()
