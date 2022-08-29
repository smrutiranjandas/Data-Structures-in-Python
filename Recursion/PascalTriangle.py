#Requirement: To Print the Pascals Triangle
#Method used: Recursion

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

def printPascalTriangle(intNum):

    if intNum == 1:
        return [[1]]
    else:
        
        listCurrentPascal = []
        listCurrentPascal.append(1)
        
        listPascal = printPascalTriangle(intNum-1)
        listlastPascal = listPascal[-1]
        
        for index in range(1, len(listlastPascal) ):
            
            Num = listlastPascal[index-1] + listlastPascal[index]
            listCurrentPascal.append(Num)
            
        listCurrentPascal.append(1)
        
        listPascal.append(listCurrentPascal)
        return listPascal
            
        
# Print Pascals Triangle from num = 1 to 10       
listPascal = printPascalTriangle(intNum=10)
for innerlist in listPascal:
    print(innerlist)
    