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

# 2D Lists
# each element in a 2D list is a list in itself.
matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
print(matrix[0][1])
# the above statement will print the element at index 1 in the element at index 0

for item in matrix:
    for number in item:
        print(number)
# iterating all the elements of a 2D list.
