from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        for tire in self.tire_wear_array:
            if tire >= 0.9:
                return True
        return False