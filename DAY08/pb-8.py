seen = ""
frequent = ""
second_frequent = ""
max_count = 0
second_count = 0

for i in range(len(text)):
    if text[i] not in seen:
        seen += text[i]
        count = 0
        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1

        if count > max_count:
            second_frequent = frequent
            second_count = max_count
            frequent = text[i]
            max_count = count
        elif count > second_count:
            second_frequent = text[i]
            second_count = count

if second_frequent:
    print(second_frequent, second_count)
