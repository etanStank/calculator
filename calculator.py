# -- TERMINAL -- #
from src.terminal import generate_input
from src.terminal import input_check

# -- SOLVING -- #

from src.solving import convert_string
from src.solving import calculate

# -- GLOBALS -- #

__version__ = "1.0.0"

# -- TERMINAL INPUT -- #
correct_input = False

# -- INFORMATION -- #  
print("Simple Python Calculator")
print("The possible operations are,\n +, \n -, \n *, \n /")

# Loop until correct_input is True
while not correct_input:
    input_string = generate_input()
    list = convert_string(input_string)
    
    check_result = input_check(list)
    
    if check_result is True:
        correct_input = True

        calculated_string = calculate(list)
        print(str(calculated_string[0]))
