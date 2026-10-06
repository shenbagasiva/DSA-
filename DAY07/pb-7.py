numbers = [1, 2, 3, 2, 3, 4, 5, 1]
count = 1
highest = 0
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        count += 1
    else:
        count = 1
    if count > highest:
        highest = count
print(highest)
