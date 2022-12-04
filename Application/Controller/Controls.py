import pygame
from Application.Controller.operators import Operators
from Application.Polyminoes import Tetrimino
from Application.Board.Board import Board
from typing import Literal
from Application.Util.tkToPygameTranslator import translator


class ControlScheme:
    _scheme = ...
    _default_keys = ...

    def update_control(self, control: Literal["down", "drop", "left", "right", "quit_key", "rotateCounter","rotatePrimary"], value: int):
        self._scheme[control] = value

    def bulk_update_controls(self, updates: dict[Literal["down", "drop", "left", "right", "quit_key", "rotateCounter","rotatePrimary"], int]):
        for control, value in updates.items():
            self.update_control(control, value)

    def get(self, control: Literal["down", "drop", "left", "right", "quit_key", "rotateCounter","rotatePrimary"]) -> int:
        return self._scheme.get(control)

    @staticmethod
    def default_scheme(): pass

    @staticmethod
    def default_keys() -> tuple: pass

    @staticmethod
    def key_list() -> list[str, str, str, str, str, str, str]:
        return ["down", "drop", "left", "right", "quit_key", "rotateCounter", "rotatePrimary"]


class TkScheme(ControlScheme):
    def __init__(self):
        super().__init__()
        self._scheme = self.default_scheme()

    def to_pygame_scheme(self):
        scheme = self._scheme
        sending_scheme = map(lambda key, val: (key, translator.tk_to_pg(val)), scheme)

        return PygameScheme.custom(**dict(sending_scheme))

    @staticmethod
    def custom(**kwargs: dict[Literal["down", "drop", "left", "right", "quit_key", "rotateCounter", "rotatePrimary"],
                              int]):
        """Call with a dictionary containing the values you want mapped. Any not mentioned values will
            have default values"""
        scheme = TkScheme()
        if kwargs is not None:
            for control, value in kwargs:
                scheme.update_control(control, value)
        return scheme

    @staticmethod
    def default_keys() -> tuple:
        return 104, 32, 100, 102, 81, 65, 98

    @staticmethod
    def default_scheme():
        return dict(zip(ControlScheme.key_list(), TkScheme.default_keys()))


class PygameScheme(ControlScheme):
    def __init__(self):
        super().__init__()
        self._scheme = self.default_scheme()

    @staticmethod
    def custom(**kwargs: dict[Literal["down", "drop", "left", "right", "quit_key",
                                      "rotateCounter", "rotatePrimary"], int]):
        """Call with a dictionary containing the values you want mapped. Any not mentioned values will
        have default values"""
        scheme = PygameScheme()
        if kwargs is not None:
            for control, value in kwargs:
                scheme.update_control(control, value)
        return scheme

    @staticmethod
    def default_keys() -> tuple:
        return pygame.K_DOWN, pygame.K_SPACE, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_q, pygame.K_a, pygame.K_d

    @staticmethod
    def default_scheme():
        return dict(zip(ControlScheme.key_list(), PygameScheme.default_keys()))


class Controls:
    @staticmethod
    def default():
        return Controls.generate()

    @staticmethod
    def generate(scheme: ControlScheme = ControlScheme()):
        return ControlMap(scheme)


class ControlMap:
    def __init__(self, scheme: ControlScheme):
        keys = scheme.key_list()
        self._quit = keys.pop(keys.index("quit_key"))
        self._keys = dict(map(lambda key: (key, scheme.get(key)), keys))
        operator_functions = (Operators.go_down, Operators.go_left, Operators.go_right,
                              Operators.drop, Operators.rotate, Operators.rotateCounter)
        self._commands = dict(zip(self._keys.values(), operator_functions))

    def __contains__(self, item):
        return item in self._commands

    def __getitem__(self, item):
        try:
            key = item if isinstance(item, int) else self._keys[item]
            return self._commands[key]
        except KeyError:
            raise KeyError("Invalid Control")

    def push(self, button, mino: Tetrimino, board: Board):
        self[button](mino, board)
