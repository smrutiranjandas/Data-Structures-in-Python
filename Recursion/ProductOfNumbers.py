# Requirements: To find product of two numbers without multiplication, using recursion

def Product(num1, num2):
    
    if num2 == 0 or num1 == 0:
        return 0
    elif num2 == 1:
        return num1
    elif num1 == 1:
        return num2
        
    else:
        
        intProduct = num1 + Product(num1, num2-1)
        return intProduct
    
    
    
num1 = 10
num2 = 24    
    
intProduct = Product(num1, num2)
print(intProduct)