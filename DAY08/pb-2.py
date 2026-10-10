text = "swiss"
word = ""

for i in range(len(text)):

    count = 0
    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1
    if count == 1:
        print(text[i])
        break
        