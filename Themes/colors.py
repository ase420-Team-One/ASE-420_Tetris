import random


class Colors:
    def __init__(self, is_dark_mode : bool = True):
        mode = self.dark if is_dark_mode else self.light
        mode()

    _colors = (
        (250, 78, 233),     # purple pizzazz
        (61, 226, 221),    # turquoise
        (255, 132, 74),       # mango tango
        (141, 255, 62),      # spring frost
        (221, 29, 96),      # ruby
        (157, 57, 238),      # purple x 11
        (31, 255,186),      # sea green crayola
        (147,255,255),       # electric blue
        (255,175,25)        # honey yellow
    )

    _background_colors = (
        (255, 204, 255),
        (255, 229, 204),
        (204, 255, 229),
        (255, 204, 229),
        (204, 204, 255),
        (229, 204, 255),
        (204, 209, 255),
        (204, 255, 255),
        (204, 255, 204),
    )

    def random(self):
        return random.randint(0, len(self._colors) -1)

    def select(self, index): return self._colors[index]

    def select_background_color(self, index): return self._background_colors[index]

    def dark(self):
        self.PRIMARY=(23,22,26)         # eerie black
        self.SECONDARY=(70,70,82)       # dark liver
        self.TERTIARY=(217,217,220)     # gainsboro

    def light(self):
        self.SECONDARY=(0,0,0)          # black
        self.PRIMARY=(255,255,255)      # white
        self.TERTIARY=(128, 128, 128)   # gray
