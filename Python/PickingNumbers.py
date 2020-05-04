
def pickingNumbers(a):
    # Write your code here
    a.sort()
    lengthOfA = len(a)
    firstHalf = a[0:lengthOfA//2]
    secondHalf = a[lengthOfA//2:lengthOfA]
    maximum = 0
    comb = ([x for x in a])
    lencomb = len(comb)
    for ix in range(len(comb)):
        print(comb[ix])
    return lencomb
    
arr = [1,1,2,2,4,4,5,5,5]
ar = [4, 6, 5, 3, 3, 1]
a = [1,2,2,1,2]
print(pickingNumbers(a))