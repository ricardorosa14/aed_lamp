from models import Lamp
from models import ColorLamp
from models import LampArray

class LampController:
    def __init__(self):
        self.lamps = []

    def add_lamp(self, id):
        lamp = Lamp()
        dic = {
            'id' : id,
            'lamp' : lamp
        }
        self.lamps.append(dic)
    
    def add_ColorLamp(self, id, color):
        lamp = ColorLamp(color)
        dic = {
            'id' : id,
            'lamp' : lamp
        }
        self.lamps.append(dic)

    def add_LampArray(self, id):
        lamp = LampArray()
        dic = {
            'id' : id,
            'lamp' : lamp
        }
        self.lamps.append(dic)


    def set_on(self, id):
        # Change lamp status to ON
        for lamp in self.lamps:
            if lamp['id'] == id:
                lamp['lamp'].set_on()

    def set_off(self, id):
        # Change lamp status to OFF
        for lamp in self.lamps:
            if lamp['id'] == id:
                lamp['lamp'].set_off()
        
    def get_status(self, id):
        # Returns True if lamp is ON
        for lamp in self.lamps:
            if lamp['id'] == id:
                return lamp['lamp'].get_status()
        