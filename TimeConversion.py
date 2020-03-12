def timeConversion(s):
    #
    # Write your code here.
    #
    ssplit = s.split(":",len(s))
    shours = ssplit[0:1][0][0:2]
    minute = ssplit[1:2][0][0:2]
    second = ssplit[2:4][0][0:2]
    suffix = ssplit[2:4][0][2:4]
    result = ""

    if suffix == "AM" and int(shours) >= 12:
        shours = int(shours) - 12
        result = "0" + str(shours) + ":" + str(minute) + ":" +  str(second)
        return result
    elif suffix == "PM" and int(shours) < 12:
        shours = int(shours) + 12
        result = str(shours) + ":" + str(minute) + ":" +  str(second)
        return result
    else:
        result = str(shours) + ":" + str(minute) + ":" +  str(second)
        return result


date = "12:45:54PM" #00:00:00

print(timeConversion(date))