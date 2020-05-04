def getMoneySpent(keyboards, drives, b):
    # Write your code here.

    arr = []
    m = len(keyboards)
    n = len(drives)
    if m < 1 or m > 1000:
        return -1
    if n < 1 or n > 1000:
        return -1
    if b < 1 or b > 1000000:
        return -1
    if len(keyboards) != 0:
        list_of_pairs = [(x, y) for x in keyboards for y in drives]

    for e1, e2 in list_of_pairs:
        if e1 + e2 <= b:
            arr.append(e1 + e2)

    if arr != []:
        return max(arr)
    else:
        return -1

kboards = [1,2,3,4]
hdrives = [2,4,6,8]
budget = 12
print(getMoneySpent(kboards, hdrives, budget))