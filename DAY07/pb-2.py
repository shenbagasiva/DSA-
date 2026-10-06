numbers = [4, 7, 2, 7, 9, 2, 5]


for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count == 1:
        print(numbers[i])
        break