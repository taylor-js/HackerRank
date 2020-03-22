def jumpingOnClouds(c):
    count = -1
    index = 0
    while index < len(c):
        count += 1
        if index < len(c)-2 and c[index+2] == 0:
            index += 1
        index += 1
    return count

arr3 = [0, 0, 0, 1, 0, 0] # 3
arr4 = [0, 0, 1, 0, 0, 1, 0] # 4
arr6 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0] # 6
print(jumpingOnClouds(arr3))
print(jumpingOnClouds(arr4))
print(jumpingOnClouds(arr6))

