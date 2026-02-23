from math_without_integers import zero_to_infinity

print("Make sure the bigger of the numbers is divisble by the smaller on")
print("Don't input too big numbers. I suggest 4 to 5 digits max")
print("Remember that the bigger number must be divisible by smaller one")
n1 = zero_to_infinity.get_string("Input the first number: ")
n2 = zero_to_infinity.get_string("Input the second number: ")

bigger = zero_to_infinity.compare_bigger(n1, n2)
smaller = zero_to_infinity.compare_smaller(n1, n2)

print("The result of addition is: ", zero_to_infinity.add(n1, n2))
print("The result of substraction is: ", zero_to_infinity.substract(bigger, smaller))
print("The result of multiplication is: ", zero_to_infinity.multiply(n1, n2))
print("The result of division is: ", zero_to_infinity.divide(bigger, smaller))

print("Now, let's see how much faster are the optimized functions")
print("Use numbers of however length you feel like, I suggest somewhere between 20 and 30 digits")

n1 = zero_to_infinity.get_string("Input the first number: ")
n2 = zero_to_infinity.get_string("Input the second number: ")

print("I will use 1 000 for unoptimized multiplication, 5 000 000 for addition and your numbers for optimized ones")
print("Let's see what will be quicker")

print("Multiplication 1 000 * 1 000 : ", zero_to_infinity.multiply("1000", "1000"))
print("Optimized multiplication", n1, "*", n2, ":", zero_to_infinity.multiply_optimized(n1, n2))

print("Addition 5 000 000 + 5 000 000 : ", zero_to_infinity.add("5000000", "5000000"))
print("Optimized addition", n1, "+", n2, ":", zero_to_infinity.add_optimized(n1, n2))