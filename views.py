from controllers import LampController

if __name__ == "__main__":
    controller = LampController()
    while True:
        line = input()
        
        if line == "":
            exit(0)
        
        commands = line.split(" ")
        
        if commands[0] == "CL":
            # Create simple lamp with ID
            lamp_id = commands[1]
            controller.create_lamp(lamp_id)
            print(f'Lamp {lamp_id} created.')
        elif commands[0] == "CCL":
            # Create color lamp with ID
            lamp_color = commands[1].capitalize()
            lamp_id = commands[2]
            controller.create_ColorLamp(lamp_id, lamp_color)
            print(f'{lamp_color} ColorLamp {lamp_id} created.')
        elif commands[0] == "CLA": 
            # Create an empty lamp array with ID
            lamp_id = commands[1]
            controller.create_LampArray(lamp_id)
            print(f'LampArray {lamp_id} created.')
        elif commands[0] == "ALA":
            # Add lamp to array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
            controller.add_lamp(lamp_id, lamp_array_id)
            print(f'{lamp_id} added to {lamp_array_id}.')
        elif commands[0] == "RLA":
            # Remove lamp from array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
            controller.remove_lamp(lamp_id, lamp_array_id)
            print(f'{lamp_id} removed from {lamp_array_id}.')
        elif commands[0] == "S":
            # Get state of ID
            lamp_id = commands[1]
            result = 'OFF'
            if controller.get_status(lamp_id):
                result = 'ON'

            print(f'{lamp_id} is {result}.')
        elif commands[0] == "ON":
            # Set ID on
            lamp_id = commands[1]
            
            if not controller.in_array(lamp_id):
                controller.set_on(lamp_id)
                print(f'{lamp_id} turned ON.')
            else:
                print("Can't change state when part of an array.")
                
        elif commands[0] == "OFF":
            # Set ID off
            lamp_id = commands[1]
            
            if not controller.in_array(lamp_id):
                controller.set_off(lamp_id)
                print(f'{lamp_id} turned OFF.')
            else:
                print(f"Can't change state when part of an array.")
                
        else:
            print("Invalid command.") 