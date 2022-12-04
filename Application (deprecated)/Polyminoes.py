import random
from Application.Themes.colors import Colors


class MinoTypeList:
    """
    To extend, just do _types + (new tuple list).       This extension is innefective, I would have to turn it into a
    list, then back to a tuple If a block's rotation doesn't change (e.g. the 2x2 block) put the same rotation twice
    to prevent rotation methods from breaking
    """

    def __init__(self):
        self._types = ((), ())

    def new(self, previous=-1):  # makes it less likely to get the same Polyominoes
        length = len(self._types) - 1
        randomchoice = random.randint(0, length)
        if randomchoice == previous:
            randomnum = random.randint(0, length)
            if randomnum > previous or randomnum < previous: return self._types[randomnum]
        return self._types[randomchoice]

    def indexOf(self, choice):
        return self._types.index(choice)

    @property
    def type_list(self):
        return self._types


class TetriminoTypeList(MinoTypeList):
    def __init__(self):
        self._types = (
            ((1, 5, 9, 13), (4, 5, 6, 7)),
            ((4, 5, 9, 10), (2, 6, 5, 9)),
            ((6, 7, 9, 10), (1, 5, 6, 10)),
            ((1, 2, 5, 9), (4, 5, 6, 10), (1, 5, 9, 8), (0, 4, 5, 6)),
            ((1, 2, 6, 10), (3, 5, 6, 7), (2, 6, 10, 11), (5, 6, 7, 9)),
            ((1, 4, 5, 6), (1, 5, 6, 9), (4, 5, 6, 9), (1, 4, 5, 9)),
            ((1, 2, 5, 6), (1, 2, 5, 6)),
        )


class PolyominoTypeList(MinoTypeList):
    def __init__(self):
        self._types = (
            ((1, 5, 9, 13), (4, 5, 6, 7)),
            ((4, 5, 9, 10), (2, 6, 5, 9)),
            ((6, 7, 9, 10), (1, 5, 6, 10)),
            ((1, 2, 5, 9), (4, 5, 6, 10), (1, 5, 9, 8), (0, 4, 5, 6)),
            ((1, 2, 6, 10), (3, 5, 6, 7), (2, 6, 10, 11), (5, 6, 7, 9)),
            ((1, 4, 5, 6), (1, 5, 6, 9), (4, 5, 6, 9), (1, 4, 5, 9)),
            ((1, 2, 5, 6), (1, 2, 5, 6)),
            ((1, 4, 5, 6, 9), (1, 4, 5, 6, 9)),
            ((0, 1, 2, 4, 5, 6, 8, 9, 10), (0, 1, 2, 4, 5, 6, 8, 9, 10)),
            ((1,), (1,)),
            ((1, 2), (1, 5)),
            ((0, 1, 2, 4, 8), (0, 1, 2, 6, 10), (2, 6, 8, 9, 10), (1, 4, 8, 9, 10)),
            ((0, 1, 2, 5, 9), (2, 4, 5, 6, 10), (1, 5, 8, 9, 10), (0, 4, 5, 6, 8)),)


# Polyminos should be extended directly from mino
class Mino:
    _type_set = None
    _type_set_list = None
    _color = None
    _rotation = 0
    _shift_x = 3
    _shift_y = 0

    def __init__(self):
        self._color = Colors().random()

    @property
    def shift_x(self): return self._shift_x

    @property
    def shift_y(self): return self._shift_y

    @shift_x.setter
    def shift_x(self, newVal): self._shift_x = newVal

    @shift_y.setter
    def shift_y(self, newVal): self._shift_y = newVal

    @property
    def color(self): return self._color

    @property
    def rotation(self): return self._rotation

    @rotation.setter
    def rotation(self, newRotation): self._rotation = newRotation % len(self._type_set)


class Tetrimino(Mino):  # Now also changes to polyomino list.
    # Each tetrimino is can appear in any spot in a 4x4 holder grid
    HOLDER_SIZE = 4

    def __init__(self, mino):
        super().__init__()
        if mino == "t":
            self._type_set_list = TetriminoTypeList()
        else:
            self._type_set_list = PolyominoTypeList()
        self._previous = None
        self._type_set = self._type_set_list.new(self._previous)

    def newMino(self):
        self._type_set = self._type_set_list.new(self._previous)
        self._previous = self._type_set_list.indexOf(self._type_set)
        self._shift_x = 3
        self._shift_y = 0
        self.rotation = 0
        self._color = Colors().random()

    @property
    def type_set(self):
        return self._type_set[self._rotation]

    @property
    def all_type_sets(self):
        return self._type_set