import pygame

from Board.Board import Board
from Themes.colors import Colors
from Polyominoes import Tetrimino
from Controller.operators import Operators
from Controller.Controls import Controls
from Data.Score import Score
from GameLevel.Level import Level
from SoundControl.sound import Sound as sound

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
    def start(self, is_dark_mode, grid_user_input, speed_user_input, control_map, soundvar, ops):
        pygame.init()
        self._colors=Colors(is_dark_mode)
        self._colors.dark()
        self._level = Level()
        # GRIDUSER_INP = grid_user_input # GridInputText.gridTextbox()
        SPEEDUSER_INP = speed_user_input # SpeedInputText.speedTextbox()
        self._clock = TetrisClock(fps=int(SPEEDUSER_INP)) #
        self._screen = TetrisScreen(screen_size=(500, 600))
        self._controls = control_map
        self._score = Score()
        self._board = Board(
            grid_square_size = 20,
            coordinate_on_screen = (100, 60),
            colors=self._colors,
            sound=soundvar
        )
        self._sound = soundvar
        self._pressing_down = False
        self._current_mino = Tetrimino()
        self._sound.game_start()
        self._operators =  ops
        self.main_loop()

    def main_loop(self):
        while True:
            if self._clock.ready_to_drop() or self._pressing_down:
                self._operators.go_down(self._current_mino, self._board)
                self.game_over_check()

            self.check_for_quit()

            for event in pygame.event.get():
                self.process_event(event)

            self.draw_board()
            self._score.write_score(self._screen, self._board.score)
            self._clock.update_clock_by_level(self._board.score)
            self._level.write_level(self._screen,  self._clock)
            self.update_screen()

    def process_event(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key in self._controls:
                self._controls.push(event.key, self._current_mino, self._board)
                if event.key == self._controls["down"]:
                    self._pressing_down = True
                if event.key == self._controls["drop"]:
                    self.game_over_check()

        if event.type == pygame.KEYUP and event.key == self._controls["down"]:
            self._pressing_down = False

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
                self._sound.game_end()
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
