# write  a python function to count lower and upper character in string
def string(s):
    d={"upper_case":0, "lower_case": 0 }
    for c in s:
        if c.isupper():
            d["upper_case"] = upper_case + 1
        elif c.islower():
            d["lower_case"]= lower_case+1
        else :
            pass
        print("the original string is:",s)
        print("the upper case charactiers are:",d["upper_case"])
        print("the lower case characters are:" ,d["lower_case"])
        string_test('Hi My Name is')
