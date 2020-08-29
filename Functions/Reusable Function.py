# Reusable Function

# COPY of Emoji Converter with Reusable Function
def convert_emoji(userIn):
    words_individual = userIn.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "😢"
    }
    output = ""
    for word in words_individual:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(convert_emoji(message))
