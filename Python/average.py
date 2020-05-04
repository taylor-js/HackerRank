def average(ar):
    total = sum([e for e in set(ar)])
    length = len(set(ar))
    return '{:.3f}'.format(total/length)

arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
print(average(arr))