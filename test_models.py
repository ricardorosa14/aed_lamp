import unittest
from models import LampArray

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.controller = LampArray()

    def test_set_color(self):
        lamp = self.controller.creatLamp()
        lamp.set_color('Red')
        self.assertEqual(lamp.get_color(), 'Red')

    def test_set_all_on(self):
        self.controller.creatLamp()
        self.controller.creatLamp()
        self.controller.set_all_on()
        self.assertTrue(self.controller.check_all_on())

    def test_set_all_off(self):
        self.controller.creatLamp()
        self.controller.creatLamp()
        self.controller.set_all_off()
        self.assertTrue(self.controller.check_all_off())


if __name__ == "__main__":
    unittest.main()