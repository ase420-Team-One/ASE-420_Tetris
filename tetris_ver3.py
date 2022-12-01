import pygame
from colors import Colors
from polyominoes import Tetrimino
from operators import Operators

class Board:
    _field = []
    # _height, _width, _grid_square_size, _coordinate_on_screen

    def __init__(self, num_rows = 20, num_columns = 10, grid_square_size = 20, coordinate_on_screen = (0,0),colors=Colors()):
        self._height = num_rows
        self._width = num_columns
        self._grid_square_size = grid_square_size
        self._coordinate_on_screen = coordinate_on_screen
        self._colors=colors

        for i in range(num_rows):
            self._field.append([-1] * num_columns)

    @property
    def size(self): return (self._height, self._width)

    @property
    def screen_coordinate(self): return self._coordinate_on_screen

    def draw_board(self, screen):
        screen.fill(self._colors.PRIMARY)
        fill_color = self._colors.SECONDARY
        
        for row in range(self._height):
            for column in range(self._width):
                field_value = self._field[row][column]
                rect_left = self._coordinate_on_screen[0] + self._grid_square_size * column
                rect_top = self._coordinate_on_screen[1] + self._grid_square_size * row
                height = self._grid_square_size
                width = self._grid_square_size

                pygame.draw.rect(screen.screen, fill_color, [rect_left, rect_top, width, height], 1)
                if field_value > -1:
                    pygame.draw.rect(screen.screen, Colors().select(field_value), [rect_left + 1, rect_top + 1, width - 2, height - 2])
    
    def draw_figure(self, screen, tetrimino):
        for row in range(Tetrimino.HOLDER_SIZE):
            for column in range(Tetrimino.HOLDER_SIZE):
                pixel = row * 4 + column
                if pixel in tetrimino.type_set:
                    rect_left = self._coordinate_on_screen[0] + self._grid_square_size * (column + tetrimino.shift_x) + 1
                    rect_top = self._coordinate_on_screen[1] + self._grid_square_size * (row + tetrimino.shift_y) + 1
                    inner_colored_square_edge_size = self._grid_square_size - 2
                    pygame.draw.rect(screen.screen, Colors().select(tetrimino.color), [rect_left, rect_top, inner_colored_square_edge_size, inner_colored_square_edge_size])
    
    """
    The holding grid looks like
    0  1  2  3
    4  5  6  7
    8  9  10 11
    12 13 14 15

    a col_num and row_num can be 0 - 3. 
    First we get the rows starting index (row_num * 4) = 0, 4, 8, or 12
    Then add the col_num (first, second, third, fourth square of each row)
    Now we have the square index. If the value in the square index is in the
    currently dropping mino's possible values (type_set), then 
        We check if:
            the current y index is below the end of the board or
            the current x index is outside rows width (right or left)
            or if the current square is not empty.
        If any of the above is true, break the loop.
    if the loop is never broken, there is no intersection.

    The row_num/col_num is needed for a proper check of the out of bounds
    """
    def intersects(self, tetrimino):
        for row_num in range(Tetrimino.HOLDER_SIZE):
            row_starting_index = row_num * tetrimino.HOLDER_SIZE
            for colNum in range(Tetrimino.HOLDER_SIZE):
                square_index = row_starting_index + colNum
                if square_index in tetrimino.type_set:
                    # out of bounds check
                    if row_num + tetrimino.shift_y > self._height - 1 or \
                        colNum + tetrimino.shift_x > self._width - 1 or \
                        colNum + tetrimino.shift_x < 0 or \
                        self._field[row_num + tetrimino.shift_y][colNum + tetrimino.shift_x] > -1:
                        return True
        return False

    def check_row_filled(self, row):
        empty_cells = 0
        for square in row:
            if square == -1:
                empty_cells += 1
        
        return empty_cells == 0

    def del_row(self, row_num):
        for row in range(row_num, 1, -1):
            for square in range(self._width):
                self._field[row][square] = self._field[row - 1][square]

    def break_lines(self):
        lines = 0
        for row_num in range(1, self._height):
            is_filled = self.check_row_filled(self._field[row_num])
            if is_filled:
                lines += 1
                self.del_row(row_num)

    def freeze(self, current_mino):
        for row_num in range(current_mino.HOLDER_SIZE):
            for col_num in range(current_mino.HOLDER_SIZE):
                if (row_num * current_mino.HOLDER_SIZE + col_num) in current_mino.type_set:
                    self._field[row_num + current_mino.shift_y][col_num + current_mino.shift_x] = current_mino.color
        self.break_lines()

        """
        the following prevents input lag from holding down
        The fact that it is a static pygame.K_DOWN event instead of
        Controls.down must be ironed out in refactoring.
        """
        pygame.event.clear(eventtype= pygame.KEYDOWN)

class Tetris_Screen:
    _screen = None

    def __init__(self, screen_size):
        self._screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Tetris")

    def add_text(self, font_type, font_size, text, render_bool, color, appearance_range):
        font = pygame.font.SysFont(font_type, font_size, True, False)
        label = font.render(text, render_bool, color)
        self._screen.blit(label, appearance_range)
        pygame.display.flip()

    def fill(self, color):
        self._screen.fill(color)
    
    @property
    def screen(self): return self._screen

class Tetris_Clock:
    _clock = pygame.time.Clock()
    _fps = None
    _counter = 0

    def __init__(self, fps = 25):
        self._fps = fps
        self._stop = False

    def tick(self):
        if not self._stop:
            self._clock.tick(self._fps)
            #always drops to 0 at appropriate time
            self._counter = (self._counter + 1) % (self._fps // 2)
    def stop(self): self._stop=True

    def ready_to_drop(self):
        return self._counter == 0

class Controls:
    def default(): 
        return Control_Scheme( down = pygame.K_DOWN, 
                                left = pygame.K_LEFT, right=pygame.K_RIGHT,
                                drop = pygame.K_SPACE, rotatePrimary = pygame.K_UP,
                                quit = pygame.K_q, rotateCounter = pygame.K_a,
                                rotateSecondary= pygame.K_d)

class Control_Scheme:
    def __init__(self, down, left, right, drop, rotatePrimary, quit,rotateSecondary, rotateCounter):
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

class Tetris:
    # _clock, _screen, _board, _controls
    def start(self):
        pygame.init()
        self._colors=Colors()
        self._colors.dark()
        self._clock = Tetris_Clock(fps = 25)
        self._screen = Tetris_Screen(screen_size=(400, 500))
        self._controls = Controls.default()
        self._board = Board( num_rows = 20, num_columns = 10, 
            grid_square_size = 20, coordinate_on_screen = (100, 60), colors=self._colors)
        self._pressing_down = False
        self._current_mino = Tetrimino("p")

        while True:
            if self._clock.ready_to_drop() or self._pressing_down:
                Operators.go_down(self._current_mino, self._board)
                self.game_over_check()

            self.check_for_quit()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case self._controls.rotate:
                            Operators.rotate(self._current_mino, self._board)
                        case self._controls.rotateSecondary:
                            Operators.rotate(self._current_mino, self._board)
                        case self._controls.rotateCounter:
                            Operators.rotateCounter(self._current_mino, self._board)
                        case self._controls.left:
                            Operators.go_left(self._current_mino, self._board)
                        case self._controls.right:
                            Operators.go_right(self._current_mino, self._board)
                        case self._controls.down:
                            # can probably be extracted, this feels horribly inefficient
                            self._pressing_down = True
                        case self._controls.drop:
                            Operators.drop(self._current_mino, self._board)
                            self.game_over_check()

                if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    self._pressing_down = False
            self.update_screen()

    def check_for_quit(self):
        if (pygame.event.peek(eventtype=pygame.QUIT)):
            exit()

    # Game over stuff
    def game_over(self):
        self._screen.add_text(font_type='Calibri', font_size=65, text="Game Over", render_bool=True, color=(255, 125, 0),
                        appearance_range=[20, 200])
        self._screen.add_text(font_type='Calibri', font_size=65, text="Enter q to Quit", render_bool=True, color=(255, 215, 0),
                        appearance_range=[25, 265])
        

        while True:
            self.check_for_quit()
            # TODO may be able to extract the following into a method similar to check for quit?
                # If so, Maybe consolidate those into a method that takes an event type and function
                # checks for the event, and executes the function if its found in the stack. Could be extrapolated for moves as well.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == self._controls.quit:
                    exit()
            self.update_screen()
    
    def update_screen(self):
        self._board.draw_board(self._screen)
        self._board.draw_figure(self._screen, self._current_mino)

        pygame.display.flip()
        self._clock.tick()

    def game_over_check(self):
        if self._board.intersects(self._current_mino):
            self._clock.stop()
            self.game_over()


        

def main():
    Tetris().start()

if __name__ == "__main__":
    main()