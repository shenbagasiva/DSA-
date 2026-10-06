numbers = [0, 5, 0, 3, 8, 0, 2]
num = []
for i in range(len(numbers)):
    if numbers[i] != 0:
        num.append(numbers[i])
for i in range(len(numbers)):
    if numbers[i] ==0 :
        num.append(numbers[i])
print(num)
    