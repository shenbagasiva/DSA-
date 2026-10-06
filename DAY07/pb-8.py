numbers = [7, 2, 9, 4, 1, 8]
diff = 0
max_diff = 0
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            diff = numbers[i] - numbers[j]
        else:
            diff = numbers[j] - numbers[i]
        if diff > max_diff:
            max_diff = diff
print(max_diff)