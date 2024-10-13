"""This file handles the terminal side of the calculator"""
# -- VARIABLES -- #

operations = [
    "+",
    "-",
    "*",
    "/",
]

# -- FUNCTIONS -- #


def generate_input():
    """https://trello.com/c/yn4xRRCA/24-input"""
    user_input = input("What would you like to calculate?\n")
    return user_input


def input_check(list):
    """https://trello.com/c/iBEXpp9t/22-input-check"""
    for item in list:
        if not (isinstance(item, int) or item in operations):
            return "Your equation contains a non-numeric value."
            break
    return True
