class BMW_M4():
    def fuel_type(self):
        print("91 Octane Gasoline, Petrol.")
    def max_speed(self):
        print("280 km/h.")
class Ferrari_488_Spider():
    def fuel_type(self):
        print("Premium Gasoline, Petrol.")
    def max_speed(self):
        print("330 km/h.")

obj_bmw = BMW_M4()
obj_ferrari = Ferrari_488_Spider()
for car in (obj_bmw, obj_ferrari):
    car.fuel_type()
    car.max_speed()