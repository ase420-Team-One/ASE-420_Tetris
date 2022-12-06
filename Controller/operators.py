from SoundControl.sound import Sound as sound

class Operators:
    def __init__(self, soundvar):
        self._sound = soundvar

    def rotate(self, tetrimino, board):
        self._sound.block_move()
        old_val = tetrimino.rotation
        tetrimino.rotation += 1
        if board.intersects(tetrimino):
            tetrimino.rotation = old_val
        
    def rotateCounter(self, tetrimino, board):
        old_val = tetrimino.rotation
        tetrimino.rotation -= 1
        if board.intersects(tetrimino):
            tetrimino.rotation = old_val

    def go_left(self, tetrimino, board):
        self._sound.block_move()
        old_val = tetrimino.shift_x
        tetrimino.shift_x -= 1
        if board.intersects(tetrimino):
            tetrimino.shift_x = old_val

    def go_right(self, tetrimino, board):
        self._sound.block_move()
        old_val = tetrimino.shift_x
        tetrimino.shift_x += 1
        if board.intersects(tetrimino):
            tetrimino.shift_x = old_val

    def go_down(self, tetrimino, board):
        self._sound.block_move()
        old_val = tetrimino.shift_y
        tetrimino.shift_y += 1
        if (board.intersects(tetrimino)):
            tetrimino.shift_y = old_val
            board.freeze(tetrimino)
            tetrimino.newMino()

    def drop(self, tetrimino, board):
        while not board.intersects(tetrimino):
            tetrimino.shift_y += 1
        tetrimino.shift_y -= 1
        board.freeze(tetrimino)
        tetrimino.newMino() 
