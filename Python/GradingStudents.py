def gradingStudents(grades):
    # Write your code here
    occurancehashmap = {}
    multipleshashmap = {}

    nextMultiple5 = 0
    multiplesOf5 = [] # [5] * len(arr)
    mapOfGrades = dict(enumerate(grades))
    resultarray = []

    for r in range(0,20):
        nextMultiple5 += 5
        multiplesOf5.append(nextMultiple5)
    for m, n in mapOfGrades.items():
        multiples = [m if m % 5 == 0 else 0 for m in multiplesOf5]
        occurances = grades.count(n)
        occurancehashmap.update({ n: occurances })
        multipleshashmap.update({ n: multiples })
        mgrades = list(mapOfGrades.values())
        closest = multiples[min(range(len(multiples)), key = lambda i: abs(multiples[i]-n))]
        iclosest =  abs(closest - n) if  n >= 38 and abs(closest - n) < 3 else n
        if n in multiples:
            resultarray.append(n)
        elif (n + iclosest) % 5 == 0:
            resultarray.append((n + iclosest))
        elif (n + iclosest) % 5 != 0:
            resultarray.append(n)
        else:
            resultarray.append(iclosest)
    return resultarray

a = [80,96,18,75,80,60,60,15,45,15,10,5,46,87,33,60,14,71,65,2,5,97,0]
case = [73,67,38,33]
print(gradingStudents(case))

# minimum diff between each element in grades and the closest multiple of 5

