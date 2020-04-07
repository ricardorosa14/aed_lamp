import unittest
from models import Lamp
from models import ColorLamp
from models import LampArray

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.lamp = ColorLamp('white')

    def test_set_color(self):
        self.lamp.set_color('Red')
        self.assertEqual(self.lamp.get_color(), 'Red')



class TestLampArray(unittest.TestCase):
    def setUp(self):
        self.lamps = LampArray()

    def test_add_lamp(self):
        lista = []
        lamp =  {'ID' : 1, 'lamp' : Lamp()}
        self.lamps.add_lamp(lamp)
        self.assertNotEqual(lista, self.lamps.get_list())

    def test_remove_lamp(self):
        lista = []
        lamp =  {'ID' : 1, 'lamp' : Lamp()}
        self.lamps.add_lamp(lamp)
        self.lamps.remove_lamp(lamp)
        self.assertEqual(lista, self.lamps.get_list())

    def test_set_on(self):
        lamp =  {'ID' : 1, 'lamp' : Lamp()}
        self.lamps.add_lamp(lamp)
        self.lamps.set_on()
        self.assertTrue(self.lamps.is_on())

    def test_set_off(self):
        lamp =  {'ID' : 1, 'lamp' : Lamp()}
        self.lamps.add_lamp(lamp)
        self.lamps.set_off()
        self.assertFalse(self.lamps.is_on())

if __name__ == "__main__":
    unittest.main()