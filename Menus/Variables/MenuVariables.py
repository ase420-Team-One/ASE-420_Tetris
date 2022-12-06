import tkinter as tk
from typing import Dict
from Controller.Controls import ControlScheme
from Menus.Variables.ControlsVariable import KeyVar


class MenuVariables:
    def __init__(self):
        self._variables: Dict[str, tk.Variable] = {}
        keys = ControlScheme.key_list()
        for key in keys:
            self._variables.setdefault(key, KeyVar(value=""))

    def __str__(self) -> str:
        item_list = ""
        for key, val in self._variables.items():
            item_list += f"{type(val)} {key} has a value of {val.get()}\n"

        return item_list

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, MenuVariables):
            return False
            
        other_vars = __o.get_all()
        if len(other_vars) != len(self._variables):
            return False

        my_vars = self.get_all()
        try:
            for key, value in my_vars.items():
                if value != other_vars.get(key):
                    return False
        except KeyError:
            return False
        return True

    def get_var(self, key: str):
        return self._variables[key]

    def get_all(self):
        """Returns a map containing the keys and values of the stored variables"""
        dict_vars = dict()
        for key, value in self._variables.items():
            dict_vars.setdefault(key, value.get())
        return dict_vars

    def get(self, key: str):
        return self._variables[key].get()

    def update(self, key: str, new_val):
        """Updates a variables value without changing its reference.\n
        If the key is valid and the new_val is a valid update, returns the key, otherwise returns None.
        """
        if self.contains_key(key):
            self._variables[key].set(new_val)

    def contains_key(self, key):
        return key in self._variables.keys()

    def contains_value(self, value):
        vals = []
        for val_var in self._variables.values():
            try:
                val = val_var.get_key()
                vals.append(val)
            except AttributeError:
                continue

        return value in vals