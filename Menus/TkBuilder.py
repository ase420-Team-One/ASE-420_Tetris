from collections.abc import Callable
from Util.WidthHeightPair import WidthHeightPair
import tkinter as tk
from tkinter import ttk
from Util.Types import *


class TkBuilder:
    def __init__(self):
        self._root = tk.Tk()

    def set_title(self, title: str):
        self._root.title(title)

    def build_geometry(self, window_dimensions: WidthHeightPair):
        """Sets the geometry of the root window. May be refactored for variable sizes.
        - Determines the displacement needed to center the screen based on screensize,
        - Sets the width/height to 300/200 respectively (will be reworked to be relative)
        - Consolidates this into a string put into the `Tk.geometry()` function.
        """
        self._root.geometry(self.build_geometry_string(window_dimensions))

    @staticmethod
    def build_geometry_string(window_dimensions: WidthHeightPair):
        return f'{window_dimensions.width}x{window_dimensions.height}'

    def build_frame(self, frame: ttk.Frame = None, padding: int = 0,
                    relief: ReliefLiteral = None,
                    fill: FillLiteral = None, expand: bool = False,
                    side: SideLiteral = None):
        holder = self._root if frame is None else frame

        frm = ttk.Frame(holder, padding=padding, relief=relief)
        frm.pack(fill=fill, expand=expand, side=side)
        return frm

    def build_button(self, frame: ttk.Frame, text_content: str, on_click: Callable[[], None]):
        holder: ttk.Frame | tk.Tk = self._root if frame is None else frame

        ttk.Button(holder, text=text_content, command=on_click).pack()

    def build_label(self, frame: ttk.Frame, text: str, side: SideLiteral = "left"):
        holder = self._root if frame is None else frame
        ttk.Label(holder, text=text).pack(side=side, padx=4)

    def build_label_frame(self, frame: ttk.Frame, text: str, padding: int = 0,
                    relief: ReliefLiteral = None, fill: FillLiteral = None, 
                    expand: bool = False, side: SideLiteral = None):
        holder = self._root if frame is None else frame
        frm = ttk.Labelframe(holder, text=text, relief=relief, padding=padding)
        frm.pack(fill=fill, expand=expand, side=side, pady=5)
        return frm

    def display(self):
        self._root.mainloop()

    def root(self):
        return self._root.frame
