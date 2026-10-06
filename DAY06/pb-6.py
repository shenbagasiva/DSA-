text = "I love learning Python programming"
current_word = "" 
longest_word = "" 
for character in text:
    if character != " ":
        current_word = current_word + character

    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""
if len(current_word) > len(longest_word):
    longest_word = current_word
print(longest_word)
print(len(longest_word))
    