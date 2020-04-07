from models import Lamp
from models import ColorLamp
from models import LampArray

class LampController:
    def __init__(self):
        self.lamps = []

    def create_lamp(self, id):
        lamp = Lamp()
        dic = {
            'ID' : id,
            'lamp' : lamp  
        }
        self.lamps.append(dic)
    
    def create_ColorLamp(self, id, color):
        lamp = ColorLamp(color)
        dic = {
            'ID' : id,
            'lamp' : lamp
        }
        self.lamps.append(dic)

    def create_LampArray(self, id):
        lamp = LampArray()
        dic = {
            'ID' : id,
            'lamp' : lamp
        }
        self.lamps.append(dic)

    def add_lamp(self, lamp_id, lamp_array_id):
        for lamp in self.lamps:
            if lamp['ID'] == lamp_array_id:
                for new_lamp in self.lamps:
                    if new_lamp['ID'] == lamp_id:
                        lamp['lamp'].add_lamp(new_lamp)
                        
    def remove_lamp(self, lamp_id, lamp_array_id):
        for lamp in self.lamps:
            if lamp['ID'] == lamp_array_id:
                for lamp_to_remove in self.lamps:
                    if lamp_to_remove['ID'] == lamp_id:
                        lamp['lamp'].remove_lamp(lamp_to_remove)


    def set_on(self, id):
        # Change lamp status to ON
        for lamp in self.lamps:
            if lamp['ID'] == id:
                lamp['lamp'].set_on() 

    def set_off(self, id):
        # Change lamp status to OFF
        for lamp in self.lamps:
            if lamp['ID'] == id:
                lamp['lamp'].set_off() 
        
    def get_status(self, id):
        # Returns True if lamp is ON
        for lamp in self.lamps:
            if lamp['ID'] == id:
                return lamp['lamp'].is_on()

    def get_lamp(self, id):
        for lamp in self.lamps:
            if lamp['ID'] == id:
                return lamp['lamp']
    
    def get_list(self, id):
        for lamp in self.lamps:
            if lamp['ID'] == id:
                return lamp['lamp'].get_list()

    
    def in_array(self, id):
        result = False
        for lamp in self.lamps:
            if type(lamp['lamp']) == LampArray:
                if lamp['lamp'].in_list(id):
                    return True
                
        return result
    