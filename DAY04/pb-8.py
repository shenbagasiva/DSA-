numbers = [5, 3, 8, 3, 9, 5, 2]

found = False

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j]:
            print("First duplicate element:", numbers[i])
            found = True
            break

    if found:
        break