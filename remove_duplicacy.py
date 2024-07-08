list1 = [4,5,6,4,6]
list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)

print(list2)