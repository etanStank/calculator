# -- TERMINAL -- #
from src.terminal import generate_input
from src.terminal import output
from src.terminal import input_check

# -- SOLVING -- #

from src.solving import convert_string
from src.solving import calculate

# -- GLOBALS -- #

__version__ = "1.2.1"

# -- TERMINAL INPUT -- #

correct_input = False

# Loops until correct_input is true
while correct_input ==  False:
    input_string = generate_input()
    list = convert_string(input_string)
    print("yes")
    
    input_check = input_check(list)
    
    if input_check:
        correct_input = True
    else:
        print(f"{input_check}\n")

    # -- SOLVING -- #

    calculated_string = calculate(list)

    # -- OUTPUT -- #

    output(str(calculated_string))