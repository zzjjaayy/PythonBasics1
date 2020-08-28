# Dictionaries
# A data type with key value pairs.

customer = {
    "name": "John",
    "age": "30",
    "is_verified": True
}
# above is a dictionary with key value pairs.

customer["name"] = "jay"
# changing the value of a key

customer["b.day"] = "jan 1"
# adding a key value pair to the dictionary.

print(customer["name"])  # will print the value associated with the key passed.
# if you pass an invalid key, the interpreter will throw an error.

print(customer.get("name", "jay"))
# this does the same thing as "[]" but just returns "None" for an invalid key
# instead of an error. The second parameter is the default value if the key is invalid.

# Random Exercise
# translate numbers entered into words.

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

userInput = input("Phone: ")
output = ""
for number in userInput:
    output += numbers.get(int(number), "!") + " "
print(output)
