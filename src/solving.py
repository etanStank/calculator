# -- OPERATIONS -- #    

operations = {
    "+": lambda numA, numB: numA + numB,
    "-": lambda numA, numB: numA - numB,
    "*": lambda numA, numB: numA * numB,
    "/": lambda numA, numB: numA / numB
}

# -- FUNCTIONS -- #

def is_operation(item):
    '''
    https://trello.com/c/49UxqLT7/30-is-operation
    '''
    return item in operations

def convert_string(input_string):
    '''
    https://trello.com/c/z2vBybXd/25-convert-string
    '''
    list = []

    for letter in input_string:
        letter = letter.strip()
        list.append(letter)
    
    try:
        while ' ' in list:
            del list[' ']
        while '' in list:
            del list['']
    except:
       return list
    
    for item in list:
        item_index = list.index(item)
        list[item_index] = int(item)

    return list

def calculate(list):
    full_index = len(list)
    while 0 < int(full_index):
        for item in list:
            if is_operation(item):
                item_index = list.index(item)
                number_before = item_index - 1
                number_after = item_index + 1
                new_number = operations[item](number_before, number_after)
                list[item_index] = new_number
                del list[item_index - 1]
                del list[item_index]  
                print(list)   
    return list