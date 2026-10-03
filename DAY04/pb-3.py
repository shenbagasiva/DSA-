numbers = [12, 5, 27, 8, 19]
largest = numbers[0]
second_largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        second_largest = largest
        largest = numbers[i]
    elif numbers[i] > second_largest and numbers[i] != largest:
        second_largest = numbers[i]
print(second_largest)