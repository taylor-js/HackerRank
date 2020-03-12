def plusMinus(n,arr):
    positive = 0
    negative = 0
    zero = 0
    newarr = []
    for val in arr:
        if val > 0:
            positive += 1
        elif val < 0:
            negative += 1
        else:
            zero += 1
    newarr.extend([positive,negative,zero])
    ls = list(map(lambda x:x/n,newarr))
    for item in ls:
        print(item)
num = 6
myarray = [-4, 3, -9, 0, 4, 1]
plusMinus(num,myarray)