#Requirement: To find integer part of base 2 log n using recursion


def findlognbase2(intNum):
    
    if intNum < 2:
        return 0
    else:
        
        quotient = intNum // 2
        
        logbase2 = 1 + findlognbase2(quotient)
        return logbase2
        
        
intNum = 130        
print(findlognbase2(intNum))