#count consonants
text = "programming"
count = 0

for character in text:
    if character == "a" or  character == "e" or character == "i" or character =="o" or character =="u":
            print()
    else:
        count += 1
   
print(count)