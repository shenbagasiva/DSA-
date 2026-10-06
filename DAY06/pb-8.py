


text = "apple banana cat coffee dog"
count = 0
word = ""
duplicate = False

for character in text:
    if character != " ":
        if character in word:
            duplicate = True
        else:
            word = word + character
    else:
        if duplicate:
            count += 1
        word = ""
        duplicate = False
print(count)