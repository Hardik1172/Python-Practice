# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class vehicle:
    def __init__(self, name,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehicle):
    pass
School_bus = bus("school volvo", 180 , 12)
print("vehicle name:", School_bus.name, "vehicle max_speed:", School_bus.max_speed, "mileage:", School_bus.mileage)