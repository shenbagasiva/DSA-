#count of vowels in sting 
text = "programming"
count = 0

for character in text:
    if character == "a" or  character == "e" or character == "i" or character =="o" or character =="u":
        count += 1
        print(character)
   
print(count)