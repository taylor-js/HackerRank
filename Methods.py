import math

def Combinations(list1,list2):
    return [(list1[i], list2[j]) for i in range(len(list1)) for j in range(len(list2))]
    #return [(x,y) for x in a for y in b]



list1 = [1,2,3]
list2 = [2,4,5]

print(Combinations(list1,list2))


dog_dictionary = {
    'name': 'Freddie',
    'age': 9,
    'is_vaccinated': True,
    'height': 1.1,
    'birth_year': 2001,
    'belongings': ['bone', 'little ball']
}
test_yourself = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]


print("Length: " + str(len('Hello!')))
print("Upper: " + 'Hello!'.upper())
print("Abs: " + str(abs(-5)))
print("Round: " + str(round(-4/3)))
print("Max: " + str(max([234,21,456,73,12])))
print("Min: " + str(min('c','a','b')))
print("Sorted: " + str(sorted(['f','d','a','l','b'])))
print("Sum: " + str(sum([4/3, 2/3, 1/3, 1/3, 1/3])))
print("Type: " + str(type(True)))
print("Lower: " + 'Hello!'.lower())
print("Strip: " + ' Mug '.strip())
print("Replace: " + 'muh'.replace('h','g'))
print('Hello World'.split(' '))
print(dog_dictionary.keys())
print(dog_dictionary.values())
print(dog_dictionary.clear())
dog_dictionary['name'] = 'Fido'
print(dog_dictionary['name'])
print(sum(test_yourself) / len(test_yourself))
print(test_yourself[round(len(test_yourself) / 2) - 1])



