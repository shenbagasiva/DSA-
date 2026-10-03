numbers = [10, 20, 10, 30, 20, 40, 10]
new_list = []
for i in range(len(numbers)):
    if numbers[i] not in new_list:
        new_list.append(numbers[i])
print(new_list)
