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
    def __init__(self, color):
        Lamp.__init__(self)
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class LampArray():
    def __init__(self):
        self.lamps = []

    def add_lamp(self, lamp):
        self.lamps.append(lamp)

    def remove_lamp(self, lamp):
        self.lamps.remove(lamp)

    def set_on(self):
        for lamp in self.lamps:
            lamp['lamp'].set_on()
    
    def set_off(self):
        for lamp in self.lamps:
            lamp['lamp'].set_off()

    def is_on(self):
        for lamp in self.lamps:
            if lamp['lamp'].is_on() == False:
                return False

        return True

    def get_list(self):
        return self.lamps

    def in_list(self, id):
        if len(self.lamps) == 0:
            return False

        for lamp in self.lamps:
            if lamp['ID'] == id:
                return True

        return False
    