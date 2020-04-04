def count_substring(string,sub_string):
    n = len(sub_string)+1
    res = {}
    count = 0
    for i in range(len(string)-1):
        res[i] = string[i: n + i - 1]
    for key,value in res.items():
        if value == sub_string:
            count += 1
    return count

print(count_substring("ABCDCDC","CDC"))