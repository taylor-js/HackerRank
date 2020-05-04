def alternate(s):
    #create a dictionary of the intersect of all elements in s
    dct = {}
    count = 0
    for index in range(len(s)):
        if s[index] not in dct:
            dct[index] = s[index]
        count = sum(x == s[index] for x in dct.values())

    return count

mystring = "beabeefeab"
print(alternate(mystring))
