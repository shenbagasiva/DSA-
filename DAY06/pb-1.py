# count the words in string 
text = "I love learning Python"
count = 0
for character in text:
    if character == " ":
        count += 1
print(count + 1)