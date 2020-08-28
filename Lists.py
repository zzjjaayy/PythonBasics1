# Lists

names = ["jay", "mouli", "bob", "shelly"]
print(names[2:4])
#  just like Strings
names[0] = "j"  # changing the value of the value at index 0
print(names)

# Program to find the largest number in a list.
number = [1, 13, 52, 14, 62, 777]
largest = number[0]
for item in number:
    if item > largest:
        largest = item
print(largest)
