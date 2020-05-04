def compareTriplets(a, b):
    alice = 0
    bob = 0
    for elem in list(zip(a,b)):

        if elem[0] > elem[1]:
            alice += 1
        elif elem[0] < elem[1]:
            bob += 1
        
    return alice, bob

arr1 = [17, 28, 30]
arr2 = [99, 16, 8]

print(compareTriplets(arr1,arr2))