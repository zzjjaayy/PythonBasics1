# Nested Loops

# print coordinates.
for x in range(4):
    for y in range(4):
        print(f"{x}, {y}")

# Challenge to print "F" with Xs with for loops
# Method1 w/ multiplication function
number = [5, 2, 5, 2, 2]
for x in number:
    print("X" * x)

# Method2 w/o multiplication function
for x in number:
    output = ""
    for count in range(x):
        output += "x"
    print(output)

