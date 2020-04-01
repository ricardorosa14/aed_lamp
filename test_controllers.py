import unittest
from controllers import LampController

class TestLampController(unittest.TestCase):
    def setUp(self):
        self.controller = LampController()
    
    def test_set_on(self):        
        self.controller.set_on()
        self.assertTrue(self.controller.get_status())
    
    def test_test_off(self):
        self.controller.set_off()
        self.assertFalse(self.controller.get_status())

if __name__ == "__main__":
    unittest.main()