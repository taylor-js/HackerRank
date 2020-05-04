def CountOfMaxNums(ar):
    ls = []
    count = 0
    maximum = max(ar)
    for elem in ar:
        if elem == maximum:
            count += 1
    return count

myarr = [3,2,1,3]
print(CountOfMaxNums(myarr))
