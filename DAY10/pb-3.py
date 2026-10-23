text1 = "listen"
text2 = "silent"
if len(text1) == len(text2):
    is_anagram = True
    for character in text1:
        count1 = 0
        count2 = 0
        for i in range(len(text1)):
            if text1[i] == character:
                count1 += 1
        for j in range(len(text2)):
            if text2[j] == character:
                count2 += 1
        if count1 != count2:
            is_anagram = False
            break
    if is_anagram :
        print("anagram")
    else:
        print("not_anagram")
else:
    print("not_anagram")
    
        