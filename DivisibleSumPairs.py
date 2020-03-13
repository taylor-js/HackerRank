def divisibleSumPairs(n,k,ar):
    count = 0
    arr = []
    n = len(ar)
    for i in range(0, n): 
        for j in range(i+1, n) : 
            if (ar[i] + ar[j]) % k == 0 and i < j:
                arr.append((ar[i], ar[j]))
                count += 1
    return len(arr)
    
myarr = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(3,myarr))