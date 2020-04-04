def set_union(setA,setB):
    union = set()
    for elem_a in setA:
        for elem_b in setB:
            if elem_a & elem_b:
                union.add(elem_a)
    return union

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {10, 1, 2, 3, 11, 21, 55, 6, 8}

s_union = set_union(setA,setB)
print(s_union)