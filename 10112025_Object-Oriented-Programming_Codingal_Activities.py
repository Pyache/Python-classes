class student:
    grade = 10
    print("Hi! I am a student fo grade", grade)
ob = student()


class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelx = vehicle(240, 18)
print("Model max speed:", modelx.max_speed)
print("Model mileage:", modelx.mileage)


class Parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot('Blu', 10)
woo = Parrot('woo', 15)
print("Blu is a", blu.species)
print("Woo is a", woo.species)
print(blu.name, 'is', blu.age, 'years old.')
print(woo.name, 'is', woo.age, 'years old.')