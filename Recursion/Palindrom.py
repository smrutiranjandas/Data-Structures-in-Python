#Requirement: To check if a string is palindrom or not
#Method used: Recursion


def isPalindrom(stringInput):
    
    if len(stringInput) == 1:
        return True
    
    elif len(stringInput) == 2:
        
        if stringInput[0] == stringInput[-1]:
            return True
        else:
            return False
            
    else:
        
        if stringInput[0] != stringInput[-1]:
            return False
        else:
            return isPalindrom(stringInput[1:-1])
    
    
listInput = ['1madam1', 'madam', 'hello', 'world', '0110']

print('stringInput', 'isPalindrom')
print('=========== =============')
for stringInput in listInput:
    print(stringInput, isPalindrom(stringInput))