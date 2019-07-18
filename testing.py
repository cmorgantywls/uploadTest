def shout(thing):
    return thing.upper()

def isLeapYear(year):
    if year%4==0:
        return True
    elif year%4!=0:
        return False
    else:
        return("That's not a year?!")

print(shout("lizzo"))
print(isLeapYear(2008))