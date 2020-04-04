import unittest
from controllers import LampController

class TestLampController(unittest.TestCase):
    def setUp(self):
        self.controller = LampController()
        self.controller.create_lamp(1)
        self.controller.create_lamp(2)
        self.controller.create_ColorLamp(3, 'white')

    def test_set_on(self):        
        self.controller.set_on(2)
        self.assertTrue(self.controller.get_status(2))
    
    def test_test_off(self):
        self.controller.set_off(2)
        self.assertFalse(self.controller.get_status(2))

if __name__ == "__main__":
    unittest.main()