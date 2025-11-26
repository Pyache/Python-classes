from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task.")
class test_class(Absclass):
    def task(self):
        print("We are inside test class task.")
test_obj = test_class()
test_obj.task()
test_obj.print(100)


from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run.")
class snake(animal):
    def move(self):
        print("I can slither.")
class dog(animal):
    def move(self):
        print("I can bark.")
class lion(animal):
    def move(self):
        print("I can roar.")
r = human()
r.move()
k = snake()
k.move()
r = dog()
r.move()
l = lion()
l.move()


class india():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most spoken language in India.")
    def type(self):
        print("India is a developing country.")
class usa():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the most spoken language in USA.")
    def type(self):
        print("USA is a developed country.")
obj_ind = india()
obj_usa = usa()
for c in (obj_ind, obj_usa):
    c.capital()
    c.language()
    c.type()