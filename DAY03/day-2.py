numbers = [1, 2, 3, 5, 6]
for i in range(len(numbers)):
    found = False
    for j in range(len(numbers)):
        if numbers[i] +1 == numbers[j]:
            found = True
            break
    if found == False:
        print(numbers[i]+1)
        break