text = "ProGramMinG"
upper_case = 0
lower_case = 0
for character in text:
    if character.isupper():
        upper_case += 1
    else:
        lower_case += 1
print(upper_case)
print(lower_case)
    