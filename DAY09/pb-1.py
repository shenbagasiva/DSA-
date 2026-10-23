numbers = [2, 4, 2, 5, 4, 7, 5]
unique =[]
for i in range(len(numbers)):
    if numbers[i] in unique:
        pass


        
    else:
        unique.append(numbers[i])
       
print(unique)