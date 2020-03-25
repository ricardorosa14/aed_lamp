class Lamp:
    def __init__(self):
        self.state = False # Lamp is off by default

    def is_on(self):
        return self.state

    def set_on(self):
        self.state = True

    def set_off(self):
        self.state = False

class ColorLamp(Lamp):
    def __init__(self):
        Lamp.__init__(self)
        self.color = 'white'

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class LampArray(ColorLamp):
    def __init__(self):
        self.lamps = []

    def creatLamp(self):
        lamp = ColorLamp()
        self.lamps.append(lamp)
        return lamp

    def set_all_on(self):
        for lamp in self.lamps:
            lamp.set_on()
    
    def set_all_off(self):
        for lamp in self.lamps:
            lamp.set_off()

    def check_all_on(self):
        for lamp in self.lamps:
            if lamp.is_on() == False:
                return False
        
        return True

    def check_all_off(self):
        for lamp in self.lamps:
            if lamp.is_on() == True:
                return False
        
        return True