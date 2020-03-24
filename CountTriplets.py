def countTriplets(arr, r):
    result = []
    arrmap = []
    progr = []
    arr.sort()
    increment = 0
    s = 1
    count = 0
    for ix in range(len(arr)-2):
        arrmap.append((tuple(arr[ix:ix+3])))
    while increment <= 5:
        s = r ** increment
        progr.append(s)
        increment += 1
    length = len(progr)
    mid = length // 2
    left = tuple(progr[0:mid:])
    right = tuple(progr[mid-1:length-1])

    for elem in arrmap:
        result.append(elem)
    return left,right,result

arr = [1,4,16,64]
r = 4

print(countTriplets(arr, r))