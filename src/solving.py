# -- FUNCTIONS -- #

def convert_string(string):
    '''
    https://trello.com/c/z2vBybXd/25-convert-string
    '''
    list = []

    for letter in string:
        list.append(letter)
    
    try:
        list.remove(" ")
    except:
        return list
    
    return list

def calculate():
    return "as"