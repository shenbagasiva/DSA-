numbers = [10, 25, 7, 40, 18]
largest = 0
second = 0
for i in range(len(numbers)):
    if numbers[i] > largest:
        second = largest 
        largest = numbers[i]
print(second)