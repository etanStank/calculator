# -- OPERATIONS -- #    

operations = {
    "+": lambda numA, numB: numA + numB,
    "-": lambda numA, numB: numA - numB,
    "*": lambda numA, numB: numA * numB,
    "/": lambda numA, numB: numA / numB
}

debug_list = []

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
       print("No spaces found")
    
    for item in list:
        item_index = list.index(item)
        try:
            list[item_index] = int(item)
        except:
         debug_list.append(f"{item} will be treated as operation.")

    return list

def calculate(list):
    full_index = len(list)
    while 0 < int(full_index):
        for item in list:
            if is_operation(item):
                item_index = list.index(item)
                number_before_index = item_index - 1
                number_after_index = item_index + 1
                
                number_before = list[number_before_index]
                number_after = list[number_after_index]

                # -- DEBUG -- #
                debug_list.append(f"Item: {item}")
                debug_list.append(f"Number Index: {item_index}")
                debug_list.append(f"Number After: {number_after}")
                debug_list.append(f"Number Before: {number_before}")

                new_number = operations[item](number_before, number_after)
                list[item_index] = new_number
                del list[item_index - 1]
                del list[item_index] 
                return list