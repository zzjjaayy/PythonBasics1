# If - Else Statements

hot = False
cold = True

# in Python , If-Else statements don't have a curly braces, they use indents
# like - if the line next to the colon is indented, it means the line needs to be executed if
# the condition before the colon is true. If the line isn't indented, the line is not part of
# the if-else block i.e its execution will not depend on the if-else statement.

if hot:
    print("It is a hot day")
print("Enjoy your day")
# in the above example:
# if "hot" is "true", both the statements will be printed.
# but if it is "false", only "Enjoy your day" will be printed.

if hot:
    print("its hot")
else:
    print("its cold")
# only one of these will be printed.

if hot:
    print("its hot")
elif cold:
    print("its cold")
else:
    print("its a lovely day")
# "elif" id short for "else if" in python

