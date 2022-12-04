from tkinter import StringVar, Misc
from Application.Util.tkToPygameTranslator import translator

class KeyVar(StringVar):
    def __init__(self, key: int = None, master: Misc = None, value: str = None,
                 name: str = None) -> None:
        super().__init__(master, value, name)
        self._key = key

    def get_key(self): return self._key

    def set_key(self, value: int):
        if value != self._key:
            self._key = value
            self.set(translator.tk_to_pg_name(value))
