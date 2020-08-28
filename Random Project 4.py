# Emoji Converter
# user inputs phrases with expressions like ":)" and ":(" and the program
# converts expressions to emoticons.

message = input(">")
wordsIndi = message.split(" ")
# the above lines returns a list of elements made form breaking down the string with " " {space}
# as a separator.

emojis = {
    ":)": "😁",
    ":(": "😢"
}

output = ""
for word in wordsIndi:
    output += emojis.get(word, word) + " "
    # the above line checks for a key:value pair and if not found returns the same word.
print(output)