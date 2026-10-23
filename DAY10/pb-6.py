numbers = [1, 2, 3, 7, 8, 9, 10, 4, 5]
current = [numbers[0]]
longest = []
for i in range(len(numbers)):
    if numbers[i] == numbers[i-1] + 1:
        current.append(numbers[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [numbers[i]]
if len(current ) > len(longest):
    longest = current 
print(longest)