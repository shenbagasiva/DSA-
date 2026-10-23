text = "python is fun to learn"
word = ""
longest_word = ""
for character in text:
    if character != " ":
        word += character

    else:
        if len(word) > len(longest_word):
            longest_word = word
        word = ""
if len(word) > len(longest_word):
    longest_word = word 
print(longest_word)