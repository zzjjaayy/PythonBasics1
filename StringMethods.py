# String Methods
# when a function is specific to an object, then it becomes a method.
# when a function is not specific to an object and can be used with different objects is called a general function.
# NOTE : use "\" to use multiline statements

course = "Python for Beginners"
print(len(course))
# the "len" function{general purpose function} gets the length of the parameter passed in.
# this is not confined just to Strings but to other objects like lists.

print(course.upper())
# "upper" function to get the alphabets in upper case.
print(course.lower())
# "lower" function to get the alphabets in lower case.

print(course.find("P"))
# the "find" function gets the index of the first instance of the parameter.
# if the parameter is not present in the target String,it will return "-1".
print(course.find("th"))
# if we pass in a String as a parameter, the method will return the index of the first character of the String passed.
# the above statement will return "2"

print(course.replace("for", "to"))
# "replace" method is to replace the first parameter with the second parameter.
print(course.replace("n", "j"))
# if there are multiple instances of the parameter, then all instances will be replaced.
print("Python" in course)  # "in" operator.
# the above expression will return a boolean value, whether the parameter is in the targeted String.

print(course.title())
# "title" method makes the first letter of all words upper case and rest as lower case.
