class Level:
    def __init__(self, level = 0):
        self.level = level
        self._score_modifier = 1 + self.level

    def update_level(self, score):
        _score = score + self._score_modifier
        if _score > 3:
            self.level = 2
        if _score > 6:
            self.level = 3
        if _score > 9:
            self.level = 4

    def get_level(self):
        return self.level

    def write_level(self, screen, text):
        text = f"Level: {text.get_clock_level()}"
        screen.add_text(
            font_type='Calibri',
            font_size=25,
            text=text,
            render_bool=True,
            color=(255, 125, 0),
            appearance_range=[0, 60])

    @staticmethod
    def level_from_setting(string: str):
        return {
            "None" : 1,
            "Level 1": 2,
            "Level 2": 3,
            "Level 3": 4
        }.get(string)
