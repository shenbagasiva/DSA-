numbers = [15, 4, 22, 8, 10]
smallest = numbers[0]
second =  numbers[0]
for i in range(len(numbers)):
    if numbers[i] < smallest:
        second = smallest
        smallest = numbers[i]
    elif numbers[i] < second and numbers[i] != smallest :
        second = numbers[i]
print(second)