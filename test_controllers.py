import unittest
from controllers import LampController

class TestLampController(unittest.TestCase):
    def setUp(self):
        self.controller = LampController()
        self.controller.create_lamp(1)
        self.controller.create_lamp(2)
        self.controller.create_ColorLamp(3, 'white')
        self.controller.create_LampArray(4)

    def test_set_on(self):        
        self.controller.set_on(2)
        self.assertTrue(self.controller.get_status(2))
    
    def test_set_off(self):
        self.controller.set_off(2)
        self.assertFalse(self.controller.get_status(2))

    def test_add_lamp(self):
        self.controller.add_lamp(1, 4)
        lista = []
        lista.append({'ID':1,'lamp':self.controller.get_lamp(1)})
        self.assertEqual(lista, self.controller.get_list(4))
    
    def test_remove_lamp(self):
        self.controller.add_lamp(1, 4)
        lista = []
        self.controller.remove_lamp(1, 4)
        self.assertEqual(lista, self.controller.get_list(4))

    def test_in_array(self):
        self.controller.add_lamp(1, 4)
        self.assertTrue(self.controller.in_array(1))
        self.assertFalse(self.controller.in_array(2))
        self.controller.remove_lamp(1, 4)
        self.assertFalse(self.controller.in_array(1))

if __name__ == "__main__":
    unittest.main()