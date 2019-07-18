def shout(thing):
    return thing.upper()
    
    #rm -rf .git == remove/break all links to original you cloned down
    #git remote show origin == is it linked to anything on github??
    #git init == initialize as a git repo
    #git status == check what needs to be updated
    # git add == add files to sync/upload to github
    # git commit -m "your message" == commit changes to the master branch on github
    #git push == push everything through to github
    #making even more messages about THINGS

def isLeapYear(year):
    if year%4==0:
        return True
    elif year%4!=0:
        return False
    else:
        return("That's not a year?!")

print(shout("lizzo"))
print(isLeapYear(2008))