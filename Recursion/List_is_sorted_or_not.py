# Requirement: To find if list is sorted or not
# Method used: Recursion

def isSorted(numList):
    
    if len(numList) == 1:
        return True
    else:
        first_element = numList[0]
        numList = numList[1:]
        
        if first_element < numList[0]:
            return isSorted(numList)
        else:
            return False
            
    
    
numList = [1, 2, 3, 4, 5, 6, 7, 0]
sorted_flag = isSorted(numList)
print(sorted_flag)