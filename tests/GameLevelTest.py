from GameLevel.Level import Level
import unittest


class GameLevelTest(unittest.TestCase):
    def test_update_level(self):
        level = Level()
        score = 4
        level.update_level(score)

        result = level.get_level()
        self.assertEqual(result, 2)

    def test_get_level(self):
        level = Level()

        result = level.get_level()
        self.assertEqual(result, 1)

