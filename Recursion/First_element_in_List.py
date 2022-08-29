# Requirement: To find the first occurence of an element in a List
# Method used: Recursion


def FindItem(listInput, intNum):
    
    if len(listInput) == 1:
        
        if listInput[0] == intNum:
            return 0
        else:
            return -1
            
    else:
        
        firstNum = listInput[0]
        listInput = listInput[1:]
        
        if firstNum == intNum:
            return 0
        else:
            
            indexNum = FindItem(listInput, intNum)
            if indexNum == -1:
                return -1
            else:
                return indexNum + 1
            


listInput = [7,3,2,5,1,0,0,0]
print(FindItem(listInput, 7))

    