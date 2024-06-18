def evennumber(list1):
    list2 = []
    for a in list1:
        if a%2 == 0:
            list2.append(a)
            return list2
        evennumber([1,2,3,4,5,6,7,8])
        print("now the list is:", list2)