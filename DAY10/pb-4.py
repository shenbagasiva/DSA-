text = "programming"
max_count = 0
most_frequent = ""
for i in range(len(text)):
    count = 0
    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1
    if count > max_count :
        max_count = count 
        most_frequent = text[i]
print(most_frequent)