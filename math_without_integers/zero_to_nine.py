# A basic function for throwing errors
def error(message):
    raise Exception(message)

# Check if the string is allowed
def check_string(number):
    if number not in ["0","1","2","3","4","5","6","7","8","9"]:
        error("Only allowed values are numbers 1-9")

# input() tailored for my usecase
def get_string(prompt):
    string = input(prompt)
    check_string(string)
    return string

# Add one
def add_one(number):
    if number == "0":
        return "1"
    elif number == "1":
        return "2"
    elif number == "2":
        return "3"
    elif number == "3":
        return "4"
    elif number == "4":
        return "5"
    elif number == "5":
        return "6"
    elif number == "6":
        return "7"
    elif number == "7":
        return "8"
    elif number == "8":
        return "9"
    elif number == "9":
        error("The code was trying to add something to 9. You submited wrong numbers")

# Substract one
def substract_one(number):
    if number == "0":
        error("The code was trying to substract something from 0. You submited wrong numbers")
    elif number == "1":
        return "0"
    elif number == "2":
        return "1"
    elif number == "3":
        return "2"
    elif number == "4":
        return "3"
    elif number == "5":
        return "4"
    elif number == "6":
        return "5"
    elif number == "7":
        return "6"
    elif number == "8":
        return "7"
    elif number == "9":
        return "8"

# This function doesn't actually count. It creates a list, to use in `for` loops
def count(number):
    result = []
    while number != "0":
        number = substract_one(number)
        result.append(number)
    return result

# Compare the numbers and output the bigger one
def compare_bigger(n1, n2):
    original_n1 = n1
    original_n2 = n2
    while n1 != "0" and n2 != "0":
        n1 = substract_one(n1)
        n2 = substract_one(n2)
    if n1 == "0":
        return original_n2
    else:
        return original_n1

# Compare the numbers and output the smaller one    
def compare_smaller(n1, n2):
    original_n1 = n1
    original_n2 = n2
    while n1 != "0" and n2 != "0":
        n1 = substract_one(n1)
        n2 = substract_one(n2)
    if n1 == "0":
        return original_n1
    else:
        return original_n2
    
# Add 2 numbers together. I included the `compare` function for performance
def add(number1, number2):
    bigger = compare_bigger(number1, number2)
    smaller = compare_smaller(number1, number2)
    for x in count(smaller):
        bigger = add_one(bigger)
    return bigger

# Substract second number from the first one
def substract(number1, number2):
    for x in count(number2):
        number1 = substract_one(number1)
    return number1

# Multiply 2 numbers
def multiply(number1, number2):
    result = "0"
    for x in count(number1):
        for x in count(number2):
            result = add_one(result)
    return(result)

# Divide 2 numbers. Yes, the cryptic error messeges are intended
def divide(number1, number2):
    result = "0"
    while number1 != "0":
        number1 = substract(number1, number2)
        result = add_one(result)
    return(result)