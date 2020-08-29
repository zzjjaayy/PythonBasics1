# Constructors for Classes
# A constructor is a function that gets called at the time of creating an object of that class.

class Point:

    # the method below is called a constructor, also called an initialisation block
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# "self" is a reference to the current object
point1 = Point(10, 20)
print(point1.a)


# Exercise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi, I am {self.name} ")


# all methods in the class have "self" parameter to use the arguments passed while creating
# the object can be used in the other methods
person = Person("jay")
person.talk()

person2 = Person("Bob")
person2.talk()
