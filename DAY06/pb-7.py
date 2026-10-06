
text = "  love learning Python programming"
current_word = ""
smallest_word = ""
for character in text:
    if character != " ":
        current_word = current_word +  character
    else:
        if smallest_word == "":
            smallest_word = current_word
        elif len(current_word) < len(smallest_word):
            smallest_word = current_word
        current_word = ""
if len(current_word) < len(smallest_word):
    smallest_word = current_word
print(smallest_word)
print(len(smallest_word))