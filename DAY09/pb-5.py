numbers = [4, -2, 7, -5, 3, -1, 6]
negative_list = []
positive_list = []
for i in range(len(numbers)):
    if numbers[i]< 0 :
        negative_list.append(numbers[i])
    if numbers[i] > 0:
        positive_list.append(numbers[i])
negative_list.sort()
positive_list.sort()
numbers.sort()
print(negative_list + positive_list)
print(numbers)