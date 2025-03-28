# Heart class for composition
class Heart:
    def __init__(self):
        print("Compsistion: Heart is created")
    def __del__(self):
        print("Destrutor: the garbage collector is now deleting the Mammal part of the object")

    def __str__(self):
        tick_status = "attached" if self.tick else "none"
        return f"Mammal (age=)"