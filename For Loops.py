# For Loops

for item in "Python":
    print(item)

for item in [1, 2, 3]:
    print(item)

# Range Object
# its an object that we can iterate over.
# SYNTAX : range(start, end, steps)
range(10)  # iterates from 0 to 9
range(5, 10)  # iterates from 5 to 9
range(5, 10, 2)  # iterates from 5 to 9 in 2 steps i.e 5, 7, 9

for item in range(0, 10, 2):
    print(item)
# will iterate over the range object.

prices = [10, 20, 30]
price = 0
for item in prices:
    price = price + item
print(price)