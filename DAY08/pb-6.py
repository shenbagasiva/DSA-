text = "banana"
seen = ""
most_frequent = ""
max_count = 0
for i in range(len(text)):
    if text[i] not in seen:
        count =0
        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1
        if count > max_count:
            most_frequent = text[i]
            max_count = count
            seen += text[i]
if most_frequent:
    print(most_frequent, max_count)