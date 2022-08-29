# Requirement: To find nth Fibonacci number
# Method used: Recursion

def findFibonacci(intNum):
    
    if intNum == 1 or intNum == 2:
        return 1
    else:
        
        intFib = findFibonacci(intNum-1) + findFibonacci(intNum-2)
        return intFib
        
# Print fibonnaci numbers from 1 to 20        
for i in range(1, 21):
    print(findFibonacci(intNum=i))