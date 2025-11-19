class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehicle):
    pass
school_bus = bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, "Maximum Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)


class person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnumber)
a = employee("Rahul", 886012, 200000, "Intern")
a.display()


# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):    
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def _init_(self):
        super() .__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Object Creation
peggy = Penguin()
peggy.whoisThis()
peggy. swim()
peggy.run()