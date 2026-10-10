text = "apple mango orange"
a_count =0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for character in text:
    if  character == "a":
        a_count += 1
    elif character == "e":
        e_count += 1
    elif character == "i":
        i_count += 1
    elif character == "o":
        o_count += 1
    elif character == "u":
        u_count += 1
print(a_count)
print(e_count)
print(i_count)
print(o_count)
print(u_count)