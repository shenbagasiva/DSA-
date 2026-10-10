text = "apple mango orange"
word =""
count = 0
for character in text:
    if character != " ":
        word += character
        if character in "aeiou":
            count += 1
    else: 
        print(word,count)
        word =""
        count = 0
print(word, count)


text = "apple mango orange"

count = 0 
for character in text :
    
    if character in "aeiou":
            count += 1
print(count)