# hash collision: Chaining (store in linked list) lookup
# best case O(1) worst case O(n) for hash getting and setting

def checkMagazine(magazine, note):
    mymag = list(magazine.split(" "))
    mynote = list(note.split(" "))
    smag = set(mymag)
    snote = set(mynote)
    diff = smag - snote
    if diff.union(snote)==smag:
        print("Yes")
    else:
        print("No")
    

m = "give me one grand today night"
n = "give one grand today"
checkMagazine(m,n)
