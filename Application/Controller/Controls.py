import pygame


class Controls:
    def default():
        return ControlScheme(
            down=pygame.K_DOWN,
            left=pygame.K_LEFT,
            right=pygame.K_RIGHT,
            drop=pygame.K_SPACE,
            rotatePrimary=pygame.K_UP,
            quit=pygame.K_q,
            rotateCounter=pygame.K_a,
            rotateSecondary=pygame.K_d)


class ControlScheme:
    def __init__(self, down, left, right, drop, rotatePrimary, quit, rotateSecondary, rotateCounter):
        self._down = down
        self._left = left
        self._right = right
        self._drop = drop
        self._rotate = rotatePrimary
        self._quit = quit
        self._rotateSecondary = rotateSecondary
        self._rotateCounter = rotateCounter

    @property
    def rotate(self): return self._rotate

    @property
    def down(self): return self._down

    @property
    def left(self): return self._left

    @property
    def right(self): return self._right

    @property
    def drop(self): return self._drop

    @property
    def quit(self): return self._quit

    @property
    def rotateSecondary(self): return self._rotateSecondary

    @property
    def rotateCounter(self): return self._rotateCounter
