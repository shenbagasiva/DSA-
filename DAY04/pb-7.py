numbers = [2, 11, 15,7]
target = 9
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+ numbers[j] == target :
            print("target found",numbers[i],"+",numbers[j])