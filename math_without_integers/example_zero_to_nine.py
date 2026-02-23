from math_without_integers import zero_to_nine

print("Make sure the bigger of the numbers is divisble by the smaller one")
n1 = zero_to_nine.get_string("Input the first number: ")
n2 = zero_to_nine.get_string("Input the second number: ")

bigger = zero_to_nine.compare_bigger(n1, n2)
smaller = zero_to_nine.compare_smaller(n1, n2)

print("The result of addition is: ", zero_to_nine.add(n1, n2))
print("The result of substraction is: ", zero_to_nine.substract(bigger, smaller))
print("The result of multiplication is: ", zero_to_nine.multiply(n1, n2))
print("The result of division is: ", zero_to_nine.divide(bigger, smaller))