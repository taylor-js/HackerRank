def split_and_join(line):
    # write your code here
    splitline = line.split(" ")
    string = ""
    string = "-".join([elem for elem in splitline])
    return string

line = "a b c d e"
print(split_and_join(line))