import math
c= 50
h =30
d = input("enter numbers :")
a = d.split(',')
result_list=[]
for numbers in d:
    q = round(math.sqrt([2*c*d]/h))
result_list.append(q)
print(result_list)