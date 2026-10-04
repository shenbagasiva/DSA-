text = "madam"
palindrome = ""
for i in range(len(text)):
    palindrome = palindrome + text[len(text) - 1 - i]
if text == palindrome:
    print("palindrome",palindrome)
else:
    print("not palindrome")
    