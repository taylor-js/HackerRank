def staircase(n):
    hashdict = {}
    stair = ""
    space = ""
    
    for i in range(n):
        stair = stair + "#"
        hashdict[i] = stair
        
    for j in reversed(range(n-1)):
        space = space + " "
        hashdict[j] = space + hashdict[j]
        
    for elem in hashdict.values():
        print(elem)

staircase(20)