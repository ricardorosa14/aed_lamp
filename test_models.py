import unittest
from models import ColorLamp

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.lamp = ColorLamp()

    def test_set_color(self):
        self.lamp.set_color('Red')
        self.assertEqual(self.lamp.get_color(), 'Red')

if __name__ == "__main__":
    unittest.main()