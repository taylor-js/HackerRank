def F(n):
    if n == 0 or n == 1:
        return n
    else:
        return F(n-1)+F(n-2)

def F(n,cache={}):
    if n in cache:
        return cache[n]
    elif n > 1:
        return cache.setdefault(n,F(n-1)+F(n-2))
    return n

for i in range(40): # index memoized function
    print(i, F(i))