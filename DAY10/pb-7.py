text = "abacbcbb"
string = ""
longest = "" 
for character in text:
    if character not in string:
        string += character
    else:
        if len(string) > len(longest):
            longest = string
            position = string.index(character)
        string = string[position + 1:] + character
if len(string ) > len(longest):
    longest = string

print(longest)