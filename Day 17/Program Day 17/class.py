
class Car:                                 # creating class Car
    pass


bmw = Car                                  # creating object bmw
bmw.speed = 300                            # initializing speed for object bmw
bmw.weight = 1000
bmw.seats = 4
print(bmw.speed)


class Jeep:
    def __init__(self, jeep_speed, jeep_weight):                # initializing attributes of the object jeep
        self.speed = jeep_speed
        self.weight = jeep_weight
        self.seats = 4

    def race_mode(self):                                        # creating methods
        self.speed += 100
        self.weight -= 100
        self.seats -= 2


tata = Jeep
model_1 = tata(80, 500)
print(model_1.speed)
print(model_1.seats)
print(model_1.weight)
model_1.race_mode()
print(model_1.speed)
print(model_1.seats)
print(model_1.weight)
