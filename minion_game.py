def minion_game(string):
    k_vowel_count = 0
    c_constanent_count = 0
    for l in range(len(string)):
        if string[l].lower() in ('a', 'e', 'i', 'o', 'u'):
            k_vowel_count += 1
        elif string[l].lower() == 'y':
            k_vowel_count += 1
            c_constanent_count += len(string)-l
        else:
            c_constanent_count += len(string)-l

    if k_vowel_count > c_constanent_count:
        print("Kevin", k_vowel_count)
    else:
        print("Stuart", c_constanent_count)

minion_game("banana")