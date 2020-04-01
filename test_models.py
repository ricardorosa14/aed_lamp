import unittest
from models import ColorLamp
from models import LampArray

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.lamp = ColorLamp("white")

    def test_set_color(self):
        self.lamp.set_color('Red')
        self.assertEqual(self.lamp.get_color(), 'Red')


class TestLampArray(unittest.TestCase):
    def setUp(self):
        self.controller = LampArray()

    def test_all_on(self):
        """
        self.controller.add_lamp(lamp)
        self.controller.add_lamp(lamp)
        self.controller.set_all_on()
        self.assertTrue(self.controller.check_all_on())
        """
        pass

    def test_all_off(self):
        """
        self.controller.add_lamp(lamp)
        self.controller.add_lamp(lamp)
        self.controller.set_all_off()
        self.assertTrue(self.controller.check_all_off())
        """
        pass

if __name__ == "__main__":
    unittest.main()