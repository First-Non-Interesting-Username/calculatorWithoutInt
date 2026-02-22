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
    number = add_one(number)
    result = []
    while number != "1":
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

    result = result.lstrip('0')
    return result if result else '0'

# Reverse string (or number)
def reverse(string):
    return string[::-1]

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

# Check if inputed number is bigger than 10, if it isn't that means it must be a digit
# Negative numbers aren't implemented yet
def is_single_digit(n):
    if compare_bigger(n, "9") == "9":
        return True
    return False
    
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
        number1 = substract(number1, number2)
        result = add_one(result)
    return(result)

# Safe index, so you won't get index errors when adding 2 number with different lengths 
def safe_index(s, i):
    try:
        return s[i]
    except IndexError:
        return "0"

# Better addition
def add_optimized(n1, n2):
    if not n1 and not n2: 
        return ""
    last_n1 = safe_index(n1, -1)
    rest_n1 = n1[:-1]
    last_n2 = safe_index(n2, -1)
    rest_n2 = n2[:-1]
    last = add(last_n1, last_n2)
    if is_single_digit(last) == False:
        last = last[1:]
        rest_n1 = add_one(rest_n1)
    result = add_optimized(rest_n1, rest_n2) + last
    return result

# Better substraction
def substract_optimized(n1, n2):
    n2 = n2 or "0"
    n1 = n1 or "0"
    if n2 == "0":
        return n1.lstrip("0") or "0"
    last_n1 = safe_index(n1, -1)
    rest_n1 = n1[:-1] or "0"
    last_n2 = safe_index(n2, -1)
    rest_n2 = n2[:-1]
    if compare_bigger(last_n1, last_n2) == last_n2 and last_n1 != last_n2:
        last_n1 = "1" + last_n1
        rest_n1 = substract_one(rest_n1)
    last = substract(last_n1, last_n2)
    result = substract_optimized(rest_n1, rest_n2) + last
    return result.lstrip("0") or "0"

# Better multiplication
def multiply_optimized(n1, n2):
    result = "0"
    n1_factor = ""
    n1_reversed = reverse(n1)
    n2_reversed = reverse(n2)
    for char_n1 in n1_reversed:
        n2_factor = ""
        for char_n2 in n2_reversed:
            temp = multiply(char_n1, char_n2)
            if temp != "0":
                temp_result = temp + n1_factor + n2_factor
                result = add_optimized(temp_result, result)
            n2_factor += "0"
        n1_factor += "0"
    return result

# Exponentiation, first number is a base and the second is an exponent
def power(number, factor):
    result = "1"
    for x in count(factor):
        result = multiply_optimized(number, result)
    return result

# Returns the factorial of the number, simple as that
def factorial(big_number):
    result = "1"
    for number in count(big_number):
        result = multiply_optimized(result, number)
    return result