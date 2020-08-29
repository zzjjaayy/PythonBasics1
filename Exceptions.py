# Handle Errors in a Python Program

# If the user enters a number, the program will run good and return "exit code 0" which means
# program completed without any errors.
# but if the user enters a string, the program will crash with "exit code 1" indicating an error.
age = int(input("Age : "))
print(age)

# fix:
try:
    age = int(input("Age : "))
    income = 10000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("invalid Value")
# try except block is similar to try catch block in "java"
# all it does is tries to execute the block of code and if it encounters an error that is
# specified, it will execute the block of code present under "except"
# the programmer need to know the type of error that the try block can throw, and specify it
# in "except". You can find the type of error by executing the code under error prone
# conditions and see the error that the compiler shows.
# you need to make different except blocks for each probable error.
