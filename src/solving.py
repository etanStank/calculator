def convert_string(string):
    # Converts string into list
    list = []

    for letter in string:
        list.append(letter)
    
    # Check for spaces
    try:
        list.remove(" ")
    except:
        return list
    
    return list

def calculate():
    return "as"