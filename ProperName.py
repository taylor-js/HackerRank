#More than 2 lines will result in 0 score. Do not leave a blank line also
def solve(s):
    splt = s.split(" ")
    return splt[0][0:1].upper() + splt[0][1:] + " " + splt[1][0:1].upper() + splt[1][1:]

s = "taylor saintable"

print(solve(s))