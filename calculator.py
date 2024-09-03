# -- PROJECT -- #
__version__ = "0.2.0"

# -- TERMINAL -- #
from src.terminal import input
from src.terminal import output
from src.terminal import input_check

# -- SOLVING -- #

from src.solving import convert_string
from src.solving import calculate

# -- GLOBALS -- #
input

# -- TERMINAL INPUT -- #

correct_input = False
list = convert_string(input)

# Loops until correct_input is true
if correct_input ==  False:
    input = input()
    input_check = input_check(list)
    
    if input_check:
        correct_input = True
    else:
        print(input_check)

# -- SOLVING -- #

calculated_string = calculate(input)

# -- OUTPUT -- #