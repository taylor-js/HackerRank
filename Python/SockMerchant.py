import math

def sockMerchant(ar):
    hashmap = {}
    dictarray = dict(enumerate(ar))
    
    for key, value in dictarray.items():
        hashmap.update({ value: ar.count(math.floor(value))//2 })

    total = sum(hashmap.values())

    return total
    
myarr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(myarr))