from SoundControl.sound import Sound as sound


class Operators:
    def rotate(tetrimino, board):
        sound.block_move()
        old_val = tetrimino.rotation
        tetrimino.rotation += 1
        if board.intersects(tetrimino):
            tetrimino.rotation = old_val

    def rotateCounter(tetrimino, board):
        old_val = tetrimino.rotation
        tetrimino.rotation -= 1
        if board.intersects(tetrimino):
            tetrimino.rotation = old_val

    def go_left(tetrimino, board):
        sound.block_move()
        old_val = tetrimino.shift_x
        tetrimino.shift_x -= 1
        if board.intersects(tetrimino):
            tetrimino.shift_x = old_val

    def go_right(tetrimino, board):
        sound.block_move()
        old_val = tetrimino.shift_x
        tetrimino.shift_x += 1
        if board.intersects(tetrimino):
            tetrimino.shift_x = old_val

    def go_down(tetrimino, board):
        old_val = tetrimino.shift_y
        tetrimino.shift_y += 1
        if (board.intersects(tetrimino)):
            tetrimino.shift_y = old_val
            board.freeze(tetrimino)
            tetrimino.newMino()

    def drop(tetrimino, board):
        while not board.intersects(tetrimino):
            tetrimino.shift_y += 1
        tetrimino.shift_y -= 1
        board.freeze(tetrimino)
        tetrimino.newMino()
