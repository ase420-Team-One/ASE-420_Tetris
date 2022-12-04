import os
import pygame as pg


class Sound(object):
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

    def game_start():
        start_sound = Sound.load_sound("start.wav")
        start_sound.play()

    def block_move():
        move_sound = Sound.load_sound("move.wav")
        move_sound.play()

    def block_place():
        place_sound = Sound.load_sound("place.wav")
        place_sound.play()

    def game_end():
        end_sound = Sound.load_sound("end.wav")
        end_sound.play()

# Functions must be called where movement, start/end game, and placement of blocks occur
