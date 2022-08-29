# Requirement: Reverse the input string
# Method: Recursion

def reverseString(stringInput):
    
    if len(stringInput) == 1:
        return stringInput
    else:
        
        reverse_string = reverseString(stringInput[1:])
        reverse_string += stringInput[0]
        return reverse_string
        
        
inputString = 'Hello World!'
print(reverseString(inputString))
