# Anagram is when characters of one string rearrange and then also another string is formed

s1 = input("enter the string 1")
s2 = input("enter the string 2")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    for x in s1:
        if not x in s2:
            print("Not Anagram")
            break
    else:
        print("Anagram")

