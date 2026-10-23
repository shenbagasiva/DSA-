text = "programming"
for i in range(len(text)):
    for j in range(i):
        if text[i] == text[j]:
            print(text[i])
            break
    else:
        continue
    break