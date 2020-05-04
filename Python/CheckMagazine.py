# hash collision: Chaining (store in linked list) lookup
# best case O(1) worst case O(n) for hash getting and setting

def checkMagazine(magazine, note):
    mymag = dict(enumerate(magazine.split(" ")))
    mynote = dict(enumerate(note.split(" ")))
    d = {}
    s = {}
    r = {}
    result = ""
    for word in mymag.values():
        count = 1
        if word not in d:
            d.update({word: count})
        else:
            d[word] += count
    
    for note in mynote.values():
        count = 1
        if note not in s:
            s.update({note: count})
        else:
            s[note] += count
    
    for note,count in d.items():
        if note in s:
            r.update({note: d[note]})
    
    if r == s:
        result = "Yes"
    else:
        result = "No"

    return result

#m = "ive got a lovely bunch of coconuts"
#n = "ive got some coconuts"

m = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
n = "elo lxkvg bg mwz clm w"
print(checkMagazine(m,n)) # 

m1 = "give me one grand today night"
n1 = "give one grand today"
print(checkMagazine(m1,n1)) # Yes

m2 = "two times three is not four"
n2= "two times two is four"
print(checkMagazine(m2,n2)) # No

m3 = "ive got a lovely bunch of coconuts"
n3= "ive got some coconuts"
print(checkMagazine(m3,n3)) # No