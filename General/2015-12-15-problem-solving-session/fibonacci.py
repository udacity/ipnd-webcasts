#Jonah's
def fib(length):
    returnlist = []
    if length == 1:
        returnlist.append(0)
        return returnlist
    elif length == 2:
        returnlist = [0,1]
        return returnlist
    else:
        currentlist = fib(length-1)
        nextnumber = currentlist[-1]+currentlist[-2]
        currentlist.append(nextnumber)
        return currentlist
        
print fib(10)
