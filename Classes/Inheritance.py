# Inheritance
# inheriting or borrowing all the methods of one class to another

class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    pass
# here the "Dog" class is inheriting the "Mammal" class
# all methods of Mammal class are accessible to Dog
# the "pass" keyword means "nothing", this is used because in Python, blocks cannot be empty.


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
# object from Dog class can use Mammal's methods.
