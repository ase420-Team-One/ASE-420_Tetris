from GridControl.grid import GridInputText
from SpeedControl.speed import SpeedInputText
import unittest


class Test(unittest.TestCase):
    def testGrid(self):
        data = ['20', '10']
        GRIDUSER_INP = GridInputText.gridTextbox()
        self.assertEqual(GRIDUSER_INP, data)

    def testSpeed(self):
        data = '25'
        SPEEDUSER_INP = SpeedInputText.speedTextbox()
        self.assertEqual(SPEEDUSER_INP, data)


if __name__ == "__main__":
    unittest.main()
