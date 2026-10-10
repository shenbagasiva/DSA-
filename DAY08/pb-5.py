text = "banana"
seen = ""
for i in range(len(text)):
    if text[i] not in seen:
        count = 0
        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1
        print(text[i],count)
        seen += text[i]
        
