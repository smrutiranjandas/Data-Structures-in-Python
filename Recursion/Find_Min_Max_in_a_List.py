# Requirement: Find miniumum and maximum value in a sequence 
# Method used: Recursion

def findMinMax(inputList):
    
    if len(inputList) == 1:
        
        min_num = max_num = inputList[0]
        return min_num, max_num
        
    else:
        
        min_num = max_num = inputList[0]
        
        min_num1, max_num1 = findMinMax(inputList[1:])
        
        if min_num > min_num1:
            min_num = min_num1
            
        if max_num < max_num1:
            max_num = max_num1
            
        return min_num, max_num
        
        
        
inputList = [5, 10, 2, 15, 7, 0]
print(findMinMax(inputList))
    