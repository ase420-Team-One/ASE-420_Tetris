class Score:
    def __init__(self):
        self.initial_score = 0

    def update_score(self, new_score):
        score = self.max_score()

        with open('scores.txt', 'w') as f:
            if new_score > int(score):
                f.write(str(new_score))
            else:
                f.write(str(score))
        return score

    def max_score(self):
        with open('scores.txt', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()
        return score

    def write_score(self, screen, score):
        score = f"Score: {score}"
        screen.add_text(
            font_type='Calibri',
            font_size=25,
            text=score,
            render_bool=True,
            color=(255, 125, 0),
            appearance_range=[0, 0])

        high_score = f"High Score: {self.max_score()}"
        screen.add_text(
            font_type='Calibri',
            font_size=25,
            text=high_score,
            render_bool=True,
            color=(255, 125, 0),
            appearance_range=[0, 30]
        )
