import math

def encryption(s):
    fl = math.floor(math.sqrt(len(s)))
    cl = math.ceil(math.sqrt(len(s)))
    res = ""
    for index in range(len(s)):
        res = '\n'.join(s[i:i + cl] for i in range(0, len(s), cl)) 
    return res
print(encryption("chillout"))