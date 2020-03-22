def storedValues(array):
    grades = []
    hashmap = {}
    for i in range(0,len(array)-1,2):
        grades.append(array[i:i+2])
        hashmap.update({ array[i+1]:array[i]})
    setmap = dict(sorted(hashmap.items(), key = lambda item: item[1]))
    setmap.popitem()
    for k,v in setmap.items():
        if v == max(setmap.values()):
            print(k)

namesGrades = [5,'Harry',37.21,'Berry',37.21,'Tina',37.2,'Akriti',41,'Harsh',39]
storedValues(namesGrades)

