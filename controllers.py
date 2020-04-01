from models import Lamp

class LampController:
    def __init__(self):
        self.lamp = Lamp()

    def set_on(self):
        self.lamp.set_on()

    def set_off(self):
        self.lamp.set_off()

    def get_status(self):
        return self.lamp.is_on()