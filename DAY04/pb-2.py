numbers = [0, 5, 0, 3, 8, 0, 2]
list = []
zeros_list = []
for i in range(len(numbers)):
    if numbers[i] != 0:
        list.append(numbers[i])
    elif numbers[i] == 0:
        zeros_list.append(numbers[i])
print(list + zeros_list)