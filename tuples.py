def tuples(n,ls):
    result = []
    hashedtuples = []
    for index in range(0,len(ls)-1,n):
        result.append(tuple(ls[index:index+n]))
    for elem in result:
        hashedtuples.append([hash(elem),(elem)])
    return hashedtuples

n = 4
ls = [1,2,3,4,5,6,7,8]
for elem in tuples(n,ls):
    print(elem)