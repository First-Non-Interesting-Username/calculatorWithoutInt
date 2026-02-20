# A basic function for throwing errors
def error(message):
    raise Exception(message)

# Check if the string is allowed
def check_string(number):
    if number.isdigit() == False:
        error("Only numbers are allowed")

# Input() tailored for my usecase
def get_string(prompt):
    string = input(prompt)
    check_string(string)
    return string

# This function doesn't actually count. It creates a list, to use in `for` loops
def count(number):
    result = []
    while number != "0":
        number = substract_one(number)
        result.append(number)
    return result

# Add one
def add_one(s):
    if not s:
        return "1"
    
    last = s[-1]
    rest = s[:-1]
    if last == '9':
        return add_one(rest) + '0'
    else:
        return rest + chr(ord(last) + 1)
    
# Substract one
def substract_one(s):
    if s == "0":
        error("The code was trying to substract something from 0. You submited wrong numbers")
    
    last = s[-1]
    rest = s[:-1]

    if last == '0':
        new_rest = substract_one(rest) if rest else ''
        result = new_rest + '9'
    else:
        result = rest + chr(ord(last) - 1)

    # remove leading zeros
    result = result.lstrip('0')
    return result if result else '0'

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
    if number2 == "0":
        error("The code was trying to divide something by 0. You submited wrong numbers")
    result = "0"
    while number1 != "0":
        substract(number1, number2)
        result = add_one(result)
    return(result)