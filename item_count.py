list1 = ['a','b','c','a','d','c','c','c','b']

result = []

for item in list1:
    if item not in result:
        result.append(item)
        count = list1.count(item)
        result.append(count)

print(result)