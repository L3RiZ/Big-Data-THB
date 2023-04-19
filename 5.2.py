class Vehicle:
    def __init__ (self, name, maximum_speed, current_mileage):
        self.name = name 
        self.maximum_speed = maximum_speed
        self.current_mileage = current_mileage

Golf = Vehicle("Golf", 230, 120000)

print(Golf.maximum_speed)

