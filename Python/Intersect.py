def intersect(set1,set2):
    isect = []
    for i in set1:
        for j in set2:
            if i == j:
                isect.append(i)
    return len(isect)

arr1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
arr2 = {10, 1, 2, 3, 11, 21, 55, 6, 8}

print(intersect(arr1,arr2))