numbers = [5, -2, 8, -7, 3, -1]
positive = 0
negative = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        positive += numbers[i]

    else:
        negative += numbers[i]
print(negative)
print(positive)


