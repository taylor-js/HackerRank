def mem_fib(n, cache={}): # cache is a series of key value pairs
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in cache: # base case
        return cache[n]
    elif n > 1: # n is assigned to index, cache[n]'s assigned to 
        return cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2)) #set the value of the dictionary
    return n

#print(F(40))

for i in range(40):
    print(i, mem_fib(i))