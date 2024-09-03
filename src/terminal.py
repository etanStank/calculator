# -- VARIABLES -- #

operations = [
    "+",
    "-",
    "*",
    "/"
]

# -- FUNCTIONS -- #

def output(calculated_output):
    print(calculated_output)

def input():
    '''
    https://trello.com/c/yn4xRRCA/24-input
    '''
    input = input("What would you like to calculate?\n")
    return input

def input_check(list):
    '''
    https://trello.com/c/iBEXpp9t/22-input-check
    '''
    try:
        for item in list:
            numeric = item.isnumeric()
            if not numeric and not operations:
                return "Your equation contains a non-numeric value." 
    except Exception:
        return str(Exception)
    return True