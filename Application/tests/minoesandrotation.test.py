import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.pardir,'Controller')))
sys.path.append(os.path.abspath(os.path.join(os.path.pardir)))

from operators import Operators
from Polyominoes import Tetrimino
from Board.Board import Board
op = Operators()
tetri = Tetrimino()
board = Board()
assert type(tetri._color) == int
assert len(tetri._type_set_list._types) == 7
assert len(tetri._type_set)>1
assert tetri._rotation == 0
assert tetri._previous == -1
assert tetri._shift_x == 3
assert tetri._shift_y == 0
assert tetri._type =="t"
typeSet = tetri.type_set
isChanging = False
for x in range(3):
    tetri.newMino()
    if tetri.type_set != typeSet:
        isChanging = True
        break
    typeSet = tetri.type_set
assert isChanging
tetri.switchType()
assert tetri._type == "p"
assert len(tetri._type_set_list._types) == 13
typeSet = tetri.type_set
isChanging = False
for x in range(3):
    tetri.newMino()
    if tetri.type_set != typeSet:
        isChanging = True
        break
    typeSet = tetri.type_set
assert isChanging
print("Polyominoes are Working")
# Only testing rotate and rotateCounter
Operators.rotate(tetri, board)
assert tetri._rotation == 1
currentRotation = typeSet[tetri.rotation]
Operators.rotateCounter(tetri,board)
assert currentRotation != tetri.type_set[tetri.rotation]
print("Rotations Working") 



