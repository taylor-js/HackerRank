def twoStrings(s1, s2):
    ls1 = set(s1)
    ls2 = set(s2)
    hmap = []
    for elem1 in ls1:
        for elem2 in ls2:
            if set(elem1) & set(elem2):
                hmap.append((set(elem1),set(elem2)))
    if len(hmap) > 0:
        return "YES"
    else:
        return "NO"
        
s1 = "abcdfg"
s2 = "abacdabcfg"
res = twoStrings(s1, s2)
print(res)