def aVeryBigSum(ar):
    total = 0
    for index in range(len(ar)):
        total += ar[index]
    return total

myar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(myar))