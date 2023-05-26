from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        for num in self.tire_wear_array:
            if num >= 0.9:
                return True
        return False