numbers = [12, 5, 8, 20, 15, 20, 9]
largest = numbers[0]
sec_largest =None 
for i in range(1,len(numbers)):
    if numbers[i] > largest:
        sec_largest = largest
        largest = numbers[i]
    elif numbers[i] < largest:
        if sec_largest is None or sec_largest < numbers[i]:
            sec_largest = numbers[i]
if sec_largest is not None:
    print(sec_largest)