from sympy import *
x = symbols('x')
expr = x + 1
x = 2  # The variable x is assigned to a value
print(expr)  # The value of expr remains the same
# even if the value of x has changed in the previous line
