def miniMaxSum(arr):
    arrsum = 0
    minimum = 0
    maximum = 0
    arr.sort()
    for index in range(len(arr)):
        arrsum += arr[index]
        minimum = arrsum - arr[index]
        maximum = arrsum - arr[len(arr)-1-index]
    return minimum,maximum

myarr = [1,3,4,5,6]
print(miniMaxSum(myarr))
