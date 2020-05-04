def CuboidCombination(X,Y,Z,N):
    ar = [] 
    p = 0 
    for i in range (X + 1):
        for j in range(Y + 1):
            for k in range(Z + 1):
                if i + j + k != N:
                    ar.append([]) 
                    ar[p] = [i, j, k] 
                    p += 1 
    return ar

print(CuboidCombination(1,1,1,2))
print(CuboidCombination(2,2,2,2))