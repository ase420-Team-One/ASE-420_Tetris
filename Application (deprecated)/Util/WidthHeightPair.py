class WidthHeightPair:
    def __init__(self, width: int, height: int) -> None:
        self._width_height = (width, height)

    @property
    def width(self):
        return self._width_height[0]

    @property
    def height(self):
        return self._width_height[1]

    @property
    def pair(self):
        return self.width, self.height
