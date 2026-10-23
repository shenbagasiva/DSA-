numbers = [3, 5, 3, 7, 5, 9, 3]
seen = []
duplicate = []
for i in range(len(numbers)):
    if numbers[i] in seen :
        if numbers[i]  not in duplicate:
            duplicate.append(numbers[i])
    else:
        seen.append(numbers[i])
for number in duplicate:
    print(number)