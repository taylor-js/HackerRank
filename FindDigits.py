def findDigits(n):
    hashmap = {}
    arraymap = []
    ntostring = str(n)
    for index in range(len(ntostring)):
        if int(ntostring[index]) != 0 and n % int(ntostring[index]) == 0:
            arraymap.append(int(ntostring[index]))
    return len(arraymap)

print(findDigits(1012))