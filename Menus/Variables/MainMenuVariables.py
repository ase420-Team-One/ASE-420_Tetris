from Menus.Variables.MenuVariables import MenuVariables
import tkinter as tk


class MainMenuVariables(MenuVariables):
    def add(self, key: str, value: tk.Variable) -> str:
        """ Adds a new key:value pair to the instance.
            If the key entered already exists, will recursively
            call with an 'i' appended to the input key until a valid key is found.
            - e.g. 'test' -> 'testi'
        """
        if not self.contains_key(key):
            self._variables.setdefault(key, value)
            return key
        else:
            return self.add(key + "i", value)

    def remove(self, key: str):
        return self._variables.pop(key)

    def __getitem__(self, key:str):
        return self.get_var(key)
