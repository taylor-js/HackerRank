# With Python, I could use a hash map, a loop, and a counter variable to store each number
# in the array as keys with the corresponding values being the occurrence/count or I can use the code below. 
# I prefer to use the code below because it gets the same job done with less code.

a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
d = {x:a.count(x) for x in a}
print(d)