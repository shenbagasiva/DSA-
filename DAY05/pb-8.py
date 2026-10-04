text = "hello world python"
result = "" 
for character in text:
    if character != " ":
        result = result + character
print(result)