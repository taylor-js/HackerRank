def equalizeArray(arr):
    hashmap = {}
    dictarray = dict(enumerate(arr))
    
    for key, value in dictarray.items():
        hashmap.update({ value: arr.count(value) })

    return len(arr) - max(hashmap.values())

ea = equalizeArray([3, 3, 2, 1, 3])
print(ea)