numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 5, 7, 8, 2]
for i in range(len(numbers1)):
    for j in range(len(numbers2)):
        if numbers1[i] == numbers2[j]:
            print(numbers1[i])
