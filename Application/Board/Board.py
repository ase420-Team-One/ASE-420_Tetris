import pygame
from Themes.colors import Colors
from Polyominoes import Tetrimino
from Themes.BackgroundColor import BackgroundColor


class Board:
    _field = []

    # _height, _width, _grid_square_size, _coordinate_on_screen

    def __init__(
            self,
            num_rows=20,
            num_columns=10,
            grid_square_size=20,
            coordinate_on_screen=(0, 0),
            colors=Colors(),
            current_mino=Tetrimino()
    ):
        self._height = num_rows
        self._width = num_columns
        self._grid_square_size = grid_square_size
        self._coordinate_on_screen = coordinate_on_screen
        self._colors = colors
        self.score = 0
        self._current_mino = current_mino

        for i in range(num_rows):
            self._field.append([-1] * num_columns)

    @property
    def size(self):
        return (self._height, self._width)

    @property
    def screen_coordinate(self):
        return self._coordinate_on_screen

    def draw_board(self, screen):
        # screen.fill(BackgroundColor().get_flashing_background())
        screen.fill(BackgroundColor().get_default_background())
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
                    pygame.draw.rect(screen.screen, Colors().select(field_value),
                                     [rect_left + 1, rect_top + 1, width - 2, height - 2])

    def draw_figure(self, screen, tetrimino):
        for row in range(Tetrimino.HOLDER_SIZE):
            for column in range(Tetrimino.HOLDER_SIZE):
                pixel = row * 4 + column
                if pixel in tetrimino.type_set:
                    rect_left = self._coordinate_on_screen[0] + self._grid_square_size * (
                                column + tetrimino.shift_x) + 1
                    rect_top = self._coordinate_on_screen[1] + self._grid_square_size * (row + tetrimino.shift_y) + 1
                    inner_colored_square_edge_size = self._grid_square_size - 2
                    pygame.draw.rect(screen.screen, Colors().select(tetrimino.color),
                                     [rect_left, rect_top, inner_colored_square_edge_size,
                                      inner_colored_square_edge_size])

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

        self.score += lines ** 2

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
        pygame.event.clear(eventtype=pygame.KEYDOWN)
