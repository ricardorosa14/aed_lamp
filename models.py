class Lamp:
    def __init__(self):
        self.state = False # Lamp is off by default

    def is_on(self):
        return self.state

    def set_on(self):
        self.state = True

    def set_off(self):
        self.state = False

class ColorLamp:
    def __init__(self):
        Lamp.__init__(self)
        self.color = "White"

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color 