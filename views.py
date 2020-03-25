from controllers import LampController

if __name__ == "__main__":
    controller = LampController()
    while True:
        line = input()

        if line == "":
            exit(0)
        
        if line == "ON":
            # Liga a lampada
            controller.set_on()
            print("Lamp status set to ON.")
        if line == "OFF":
            # Desliga a lampada
            pass
        if line == "STATUS":
            # Mostra estado da lampada
            pass
