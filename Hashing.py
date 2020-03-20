class HashTable: 
    def __init__(self):
        self.dictionary = {}

    def add(self, key, value):
        self.dictionary[key] = value

    def printHT(self):
        return self.dictionary

    def search(self, item):
        for key,value in self.dictionary.items():
            if key == item:
                return value

if __name__ == '__main__':
    ht = HashTable()
    ht.add('First Name', 'Brian')
    ht.add('Last Name', 'Stephenson')
    ht.add('Age', '33')
    ht.add('Gender', 'Male')
    ht.add('Race', 'Black')
    ht.add('Country', 'United States')
    ht.add('Email Address', 'Brian.Stephenson@mail.com')

    print(ht.search('First Name'))
    print(ht.search('Gender'))
    print(ht.search('Country'))