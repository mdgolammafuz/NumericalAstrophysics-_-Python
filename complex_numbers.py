
# Understand the symbolic variable and an
from sympy import *

x = Symbol('x')
y, z = symbols('y z')

print(x + y + z)

b = Symbol('x')
print(sqrt(b**2))
b = Symbol('x', real=True, positive=True)


c = 2+5*I
print(c)
print(I**2)


# conversion of type
a = 2+5*I
print("Type of a is", type(a))

complex_number = complex(a)  # converting x to Python complex type
print("Type of y is", type(complex_number))
