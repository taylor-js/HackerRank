import string
def pangrams(s):
    alpha = list(string.ascii_lowercase)
    myString = s.replace(' ','').lower()
    sToList = list(dict.fromkeys(myString))
    sToList.sort()
    if sToList == alpha:
        return "pangram"
    else:
        return "not pangram"

sentence = 'We promptly judged antique ivory buckles for the next prize'
print(pangrams(sentence))