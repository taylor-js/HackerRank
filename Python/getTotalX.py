def getTotalX(a, b):
    between = []
    result = [(a[i], b[j]) for i in range(len(a)) for j in range(len(b))]
    return result

# set_a = {2, 6}
# set_b = {24, 36}

set_a = [2, 4]
set_b = [16, 32, 96]
print(getTotalX(set_a, set_b))
# 3
