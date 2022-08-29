#Requirement: Given a string input find all combinations of its characters ( or all subset of strings)
#Method used: Recursion

def powerset(stringInput):
    
    if len(stringInput) == 1:
        return [stringInput]
    else:
        
        unique_string_input = set(stringInput)
        unique_string_input = ''.join(unique_string_input)
        
        list_subset_string = powerset(unique_string_input[1:])
        first_character = unique_string_input[0]
        
        list_new_subset = [first_character] + list_subset_string
        for temp_string in list_subset_string:
            
            list_new_subset.append(first_character + temp_string)
            
        return list_new_subset
        
        

listInput = ['abcdef', 'hello', '43256', 'madam']

for stringInput in listInput:
    
    print(stringInput)
    print(powerset(stringInput))
    print('Total no of powerset', len(powerset(stringInput)))
    print('')