from Data.Score import Score
import unittest


class ScoreTest(unittest.TestCase):
    def test_initial_level(self):
        score = Score()
        result = score.initial_score
        self.assertEqual(result, 0)
