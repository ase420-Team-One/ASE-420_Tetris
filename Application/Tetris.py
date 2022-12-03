import pygame

from Application.Board.Board import Board
from Application.Themes.colors import Colors
from Application.Polyominoes import Tetrimino
from Application.Controller.operators import Operators
from Application.Controller.Controls import Controls
from Application.Data.Score import Score
from Application.GameLevel.Level import Level

class TetrisScreen:
    _screen = None

    def __init__(self, screen_size):
        self._screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Tetris")

    def add_text(self, font_type, font_size, text, render_bool, color, appearance_range):
        font = pygame.font.SysFont(font_type, font_size, True, False)
        label = font.render(text, render_bool, color)
        self._screen.blit(label, appearance_range)

    def fill(self, color):
        self._screen.fill(color)

    @property
    def screen(self): return self._screen


class TetrisClock:
    _clock = pygame.time.Clock()
    _fps = None
    _counter = 0

    def __init__(self, fps = 25):
        self._fps = fps
        self._stop = False
        self._level = 1

    def get_clock_level(self):
        return self._level

    def update_clock_by_level(self, score):
        if score > 2:
            self._level = 2
        if score > 4:
            self._level = 3
        if score > 6:
            self._level = 4
        if score > 8:
            self._level = 5

    def tick(self):
        if not self._stop:
            self._clock.tick(self._fps)
            #always drops to 0 at appropriate time
            self._counter = (self._counter + 1) % (self._fps // self._level // 2)
    def stop(self): self._stop=True

    def ready_to_drop(self):
        return self._counter == 0


class Tetris:
    # _clock, _screen, _board, _controls
    def start(self):
        pygame.init()
        self._colors=Colors()
        self._colors.dark()
        self._level = Level()
        self._clock = TetrisClock(fps = 25)
        self._screen = TetrisScreen(screen_size=(400, 500))
        self._controls = Controls.default()
        self._score = Score()
        self._board = Board(
            num_rows = 20,
            num_columns = 10,
            grid_square_size = 20,
            coordinate_on_screen = (100, 60),
            colors=self._colors
        )
        self._pressing_down = False
        self._current_mino = Tetrimino()

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

            self.draw_board()
            self._score.write_score(self._screen, self._board.score)
            self._score.update_score(self._board.score)

            self._clock.update_clock_by_level(self._board.score)
            self._level.write_level(self._screen,  self._clock)
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

    def draw_board(self):
        self._board.draw_board(self._screen)
        self._board.draw_figure(self._screen, self._current_mino)

    def update_screen(self):
        pygame.display.flip()
        self._clock.tick()

    def game_over_check(self):
        if self._board.intersects(self._current_mino):
            self._clock.stop()
            self.game_over()
    def minoSwitch(self): # Added for switching mino types.
        self._current_mino.switchType()