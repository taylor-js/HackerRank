def jumpingOnClouds(c):
    count = -1
    i = 0
    while i < len(c):
        count += 1
        if i < len(c)-2 and c[i+2] == 0:
            i += 1
        i += 1
    return count

arr3 = [0, 0, 0, 1, 0, 0] # 3
arr4 = [0, 0, 1, 0, 0, 1, 0] # 4
arr6 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0] # 6
print(jumpingOnClouds(arr3))
print(jumpingOnClouds(arr4))
print(jumpingOnClouds(arr6))

