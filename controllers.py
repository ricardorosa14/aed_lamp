from models import Lamp

class LampController:
    def __init__(self):
        self.lamps = []

    def add_lamp(self, id, lamp):
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
        