# Function Parameters
# NOTE : Difference between Arguments and Parameters :
# Parameters are the placeholders that are defined in the function
# Arguments are the value that is passed while calling the function.

def greet_name(first_name, last_name):
    print(f"hi {first_name} {last_name}")
# Defining the Function
# first_name and last_name are parameters


greet_name("Jay", "Rathod")  # calling the function and passing the parameters required.
# "jay" "rathod" are the arguments
# the above is an example with positional arguments i.e their position matters.

greet_name(last_name="Rathod", first_name="Jay")
# the above is an example of keyword arguments whose position doesn't matter.
