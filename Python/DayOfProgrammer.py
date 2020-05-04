def isLeapYear(year):
    if ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return True
    else:
        return False

def dayOfProgrammer(year):
    feb = 29 if isLeapYear(year) else 28 # returns 28 for year 1700
    numOfDaysMonthInRegOrLeap1919Plus = [31,feb,31,30,31,30,31,31,30,31,30,31]
    total = sum(days for days in numOfDaysMonthInRegOrLeap1919Plus[0:8])
    monthsToDays = 256 - total
    if isLeapYear(year) == True and year != 1918:
        return str(monthsToDays) + ".09." + str(year)
    elif isLeapYear(year) == False and year != 1918:
        return str(monthsToDays) + ".09." + str(year)
    else:
        return "26.09." + str(year)

print(dayOfProgrammer(2017)) # (13.09.2017)

print(dayOfProgrammer(1700)) # (12.09.1700)
print(dayOfProgrammer(1800)) # (12.09.1800)
print(dayOfProgrammer(1900)) # (12.09.1900)
print(dayOfProgrammer(1918)) # (26.09.1918)