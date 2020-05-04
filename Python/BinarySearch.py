import math

def binarySearch(array,num):
    left = 0
    right = len(array)
    while (left <= right):
        mid = left + math.floor((right-left)/2)
        if array[mid] == num:
            return mid
        if array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [4,3,1,7,2,5]
print(binarySearch(arr,3))