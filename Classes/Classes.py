# Classes
# Classes are blueprints and Objects are instances based on that blueprint.

# naming convention for variables and functions is all lower case and separated.
# naming convention for classes is camel casing
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# below is OBJECT defined and stored in a variable
point1 = Point()
# the variable then can be used to call the methods inside the class
point1.draw()
point1.move()

# an object can have attributes too, attributes are like variables specific to an object
point1.x = 10
point1.y = 20
print(point1.x)
