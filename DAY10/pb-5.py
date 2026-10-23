numbers = [0, 5, 0, 3, 8, 0, 2]
list = []
zeros = []
for i in range(len(numbers)):
    if numbers[i] != 0:
        list.append(numbers[i])
    if numbers[i] == 0:
        zeros.append(numbers[i])

   
    

print(list + zeros)