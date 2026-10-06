#find thenumbers > than the average 
numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
average = total / len(numbers)

count = 0

for i in range(len(numbers)):
    if numbers[i] > average:
        count += 1
print(count)
print(average)
