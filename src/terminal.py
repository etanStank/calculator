operations = [
    "+",
    "-",
    "*",
    "/"
]

def output(calculated_output):
    print(calculated_output)

def input():
    input = input("What would you like to calculate?\n")
    return input

def input_check(list):
    try:
        for item in list:
            numeric = item.isnumeric()
            if not numeric and not operations:
                return "Your equation contains a non-numeric value." 
    except Exception:
        return str(Exception)
    return True