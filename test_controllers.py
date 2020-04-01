import unittest
from controllers import LampController

class TestLampController(unittest.TestCase):
    def test_set_on(self):
        controller = LampController()
        controller.add_lamp("white")
        controller.set_on("white")
        self.assertTrue(controller.get_status("white"))
    
    def test_test_off(self):
        controller = LampController()
        controller.add_lamp("white")
        controller.set_off("white")
        self.assertFalse(controller.get_status("white"))

if __name__ == "__main__":
    unittest.main()