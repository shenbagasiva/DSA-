numbers = [4, -2, 7, -5, 9, -1, 3]
negative_list = []
positive_list = []
for i in range(len(numbers)):
    if numbers[i]< 0:
        negative_list.append(numbers[i])
    else:
        positive_list.append(numbers[i])
print(negative_list + positive_list)