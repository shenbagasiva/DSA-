text = "apple banana ant mango avocado"
count = 0
word = ""
for character in text:
    if character != " ":
        word = word + character
    else:
        if word[0] == "a":
            count += 1
        word = ""
if word[0] == "a":
    count += 1
print(count)