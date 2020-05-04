def mutate_string(string, position, character):
    edited = ""
    edited = string[:position] + character + string[position+1:]
    return edited

print(mutate_string("abracadabra", 5, "k"))