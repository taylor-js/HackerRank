def runnerUpScore(arr):
    s = list(set(arr))
    s.sort()
    for elem in reversed(s):
        if elem == max(arr):
            return s[len(s)-2]
        else:
            return elem

arr2 = [2, 3, 6, 6, 5] # 5
arr = [57, 57, -57, 57]
print(runnerUpScore(arr))

