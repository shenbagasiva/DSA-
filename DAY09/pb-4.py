numbers = [1, 2, 3, 5, 6, 7]
for i in range(len(numbers) - 1):
    if numbers[i] + 1 in numbers:
        pass
    else:
        print(numbers[i] + 1)