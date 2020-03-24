def storedValues(array):
    hashmap = {}
    arraymap = {}
    for i in sorted(range(len(array))):
        hashmap.update({ array[i][0]:array[i][1] })
    for key,value in hashmap.items():
        if value != min(hashmap.values()):
            arraymap.update({ key:value })
    newmin = min(arraymap.values())
    newmins = [elem[0] for elem in arraymap.items() if elem[1] == newmin]
    return newmins

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
print(storedValues(students))

