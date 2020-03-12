def countingValleys(n,s):

    land = 0
    valley = 0
    for position in s:
        if position == 'U':
            land += 1
            if land == 0:
                valley += 1
        else:
            land -= 1
            
    return valley


num = 8
journey = "UDDDUDUU"
print(countingValleys(num,journey))