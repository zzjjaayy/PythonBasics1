# python has functions for type conversion
# int() for changing the parameter from string to integer
# similarly bool() for boolean; float() for floating point.

birthYear = input("Birth year : ")
# the above input type will return a string which needs to converted to other data types for different operations.
print(type(birthYear))
# type() function returns the type of the data type of the parameter passed in.
# prints <class 'str'>
age = 2020 - int(birthYear)
# the String(str) is being converted to int.
# REMEMBER : int and float can be dealt with by python automatically, you don't need to covert its type.
print(age)
