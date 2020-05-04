import textwrap

def wrap(string, max_width):
    res = {}
    for i in range(0,len(string),max_width):
        res[i] = string[i: max_width + i]
    return res

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width = 4
tw = textwrap.wrap(string, width=4)
print(tw)

