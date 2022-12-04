class Operators:
    @staticmethod
    def rotate(tetrimino, board):
        old_val = tetrimino.rotation
        tetrimino.rotation += 1
        if board.intersects(tetrimino):
            tetrimino.rotation = old_val

    @staticmethod
    def rotateCounter(tetrimino, board):
        old_val = tetrimino.rotation
        tetrimino.rotation -= 1
        if board.intersects(tetrimino):
            tetrimino.rotation = old_val

    @staticmethod
    def go_left(tetrimino, board):
        old_val = tetrimino.shift_x
        tetrimino.shift_x -= 1
        if board.intersects(tetrimino):
            tetrimino.shift_x = old_val

    @staticmethod
    def go_right(tetrimino, board):
        old_val = tetrimino.shift_x
        tetrimino.shift_x += 1
        if board.intersects(tetrimino):
            tetrimino.shift_x = old_val

    @staticmethod
    def go_down(tetrimino, board):
        old_val = tetrimino.shift_y
        tetrimino.shift_y += 1
        if board.intersects(tetrimino):
            tetrimino.shift_y = old_val
            board.freeze(tetrimino)
            tetrimino.newMino()

    @staticmethod
    def drop(tetrimino, board):
        while not board.intersects(tetrimino):
            tetrimino.shift_y += 1
        tetrimino.shift_y -= 1
        board.freeze(tetrimino)
        tetrimino.newMino()