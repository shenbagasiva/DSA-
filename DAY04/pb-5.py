numbers = [4, 2, 7, 2, 9, 4, 3]

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if i!= j and numbers[i] == numbers[j]:
            count += 1
    if count == 0 :
        print(numbers[i])
        break