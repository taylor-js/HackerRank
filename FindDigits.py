def findDigits(n):
    hashmap = {}
    countarr = []
    valarr = []
    dictarray = dict(enumerate(n))
    #use a dictionary to figure out how many times a digit satisfies the conditions
    for key, value in dictarray.items():
        v = str(value).split()
        hashmap.update({ value: [] })
        for i in range(len(v)):
            hashmap[value].extend(list(map(int, v[i])))
            countarr.append(hashmap[value])
            valarr.append(value)
    for j in range(len(valarr)):
        res = sum(1 if elem != 0 and valarr[j] % elem == 0 else 0 for elem in countarr[j])
        print(res)
    print(dictarray)


arr = [2,12,1012]
findDigits(arr)
