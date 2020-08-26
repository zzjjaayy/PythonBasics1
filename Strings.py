str1 = "Python's course for beginners"
# if you want to use single quotes inside the string then, enclose the string value with double quotes and vice-a-versa
# In normal cases both "single" and "double" quotes are same for a string declaration
str2 = '''
Hi, Jay 

Its very nice meeting you!
'''
# "triple" quotes are for multiline Strings which is not possible with single or double quotes.
str3 = 'Python course for beginners'
print(str3[0])  # prints "P" which is the character at index 0 in string "str3"
print(str3[6])  # prints " "{white space} which is the character at index 6 in string "str3"
# python supports negative indexing which starts the characters from the end of the String
print(str3[-3])  # prints "e" which is the character at index 3 from the end in string "str3"

# print(string[x:y]) prints all characters from index "x" to one before "y"
print(str3[0:3])  # prints "Pyt" that is from index 0 to 2
print(str3[0:])  # prints all characters from index 0
print(str3[:5])  # prints all characters form start to index 4
print(str3[:])  # this syntax will just print all the characters in the string
print(str3[1:-1])  # this will print all characters from index 1 to -2 {one before -1}
# NOTE : in the above statement the order of characters will not be changed i.e straight as the string is written
