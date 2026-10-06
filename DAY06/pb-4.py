text = "I love coding every single day"
word = ""
count = 0
for character in text:
    if character != " ":
        word = word + character
    

    else:
        if len(word) == 5:
            count += 1
        word =""

if len(word) == 5:
    count += 1

print(count)
