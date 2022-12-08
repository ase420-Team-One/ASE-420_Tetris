import os
import pygame as pg


class Sound(object):
    def __init__(self, sound_is_on: bool):
        self._state : SoundState = SoundStateOn() if sound_is_on else SoundStateOff()

    def load_sound(self, file):
        """ because pygame can be be compiled without mixer.
    """
        self._state.load_sound(file)
    #Called when game initializes
    def game_start(self):
        self._state.game_start()
    #Called when user moves a piece
    def block_move(self):
        self._state.block_move()
    #Called when a piece is placed upon the board
    def block_place(self):
        self._state.block_place()
    #Called when the game has ended
    def game_end(self):
        self._state.game_end()

# Functions must be called where movement, start/end game, and placement of blocks occur

class SoundState:
    def load_sound(file): pass
    def game_start(self): pass
    def block_move(self): pass
    def block_place(self): pass
    def game_end(self): pass
    def _play_sound(self, path: str): pass

class SoundStateOn(SoundState):
    def load_sound(file):
        """ because pygame can be be compiled without mixer.
        """
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        if not pg.mixer:
            return None
        file = os.path.join(main_dir, "sound", file)
        try:
            sound = pg.mixer.Sound(file)
            sound.set_volume(0.5)
            return sound
        except pg.error:
            print("Warning, unable to load, %s" % file)
        return None
    def game_start(self): self._play_sound("start.wav")
    def block_move(self): self._play_sound("move.wav")
    def block_place(self): self._play_sound("place.wav")
    def game_end(self): self._play_sound("end.wav")
    def _play_sound(self, path: str):
        sound_clip = Sound.load_sound(path)
        sound_clip.play()

class SoundStateOff(SoundState):
    def load_sound(file): pass
    def game_start(self): pass
    def block_move(self): pass
    def block_place(self): pass
    def game_end(self): pass
    def _play_sound(self, path: str): pass
