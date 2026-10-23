numbers = [8, 3, 12,  6, 4]
number =[numbers[0]]
for i in range(len(numbers)):
    if numbers[i] < number[0]:
        number[0] = numbers[i]
print(number[0])