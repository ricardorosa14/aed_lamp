#from models import Lamp
from models import ColorLamp
from models import LampArray

class LampController:
    def __init__(self):
        self.controller = LampArray()

    def add_lamp(self, color):
        lamp = ColorLamp(color)
        self.controller.add_lamp(lamp)

    def set_on(self, color):
        # Change lamp status to ON
        for lamp in self.controller.lamps:
            if lamp.get_color() == color:
                lamp.set_on()

    def set_off(self, color):
        # Change lamp status to OFF
        for lamp in self.controller.lamps:
            if lamp.get_color() == color:
                lamp.set_off()

    def get_status(self, color):
        # Returns True if lamp is ON
        #return self.lamp.is_on()
        for lamp in self.controller.lamps:
            if lamp.get_color() == color:
                return lamp.is_on()