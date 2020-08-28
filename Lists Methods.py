# List Methods

number = [5, 2, 1, 7, 4]
number.append(20)
# method for adding a element at the end of the list
print(number)

print(number.index(5))
# gets the element's index.
print(5 in number)  # returns a boolean oer the existence of the number passed.

print(number.count(5))
# gets the number of instances of the number passed in.

number.sort()
print(number)
# sorts the order in ascending order
# use "reverse" function after "sort" to arrange in descending order.
number.reverse()
print(number)

number.insert(2, 5)
# "insert" method is for adding an element at a specific index
# SYNTAX : .insert(index, object_to_be_inserted)
print(number)

number.remove(5)
# "remove" method removes the first instance of the parameter in the list
print(number)

number.pop()
# removes the last item at the list
print(number)

number.clear()
# removes all elements in the list.

number1 = number.copy()
number2 = number

# RANDOM EXERCISE:
#  Remove duplicates from a list
# NOTE : do not remove elements from a list you are looping over.

list1 = [5, 5, 7, 5, 8, 7, 9, 8, 8]
unique = []
for number in list1:
    if number not in unique:
        unique.append(number)

print(unique)



