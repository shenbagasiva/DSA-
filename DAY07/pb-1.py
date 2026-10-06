numbers = [4, 7, 2, 7, 9, 2, 5]
num = []
duplicate = False
for i in range(len(numbers)):
    if numbers[i] in num :
        duplicate = True
        print(numbers[i])
        break
    else:
        num = num + [numbers[i]]
