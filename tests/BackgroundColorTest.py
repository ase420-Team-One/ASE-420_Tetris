from Themes.BackgroundColor import BackgroundColor
import unittest


class BackgroundColorTest(unittest.TestCase):
    def test_default_background(self):
        background = BackgroundColor()

        result = background.get_default_background()

        self.assertEqual(result, (255,255,255))
