# first things first, import NumPy
import numpy as np
# Let's create two arrays using the arange() method
array1 = np.arange(0, 5)
array2 = np.arange(0, 5)

print("Actual Arrays (Array1): ", array1)
print("Actual Arrays (Array2): ", array2)

# Adding two arrays
print("Sum of arrays : ", (array1 + array2))

# Subtracting two arrays
print("Subtraction of array : ", (array1 - array2))

# Multiplication
print("Multiplication : ", (array1 * array2))

# Division
print("Division : ", (array1 / array2))
# warning and 0/0 is replaced with nan

# Power of all elements in the array
print("Power : ", (array1 ** 2))


print("Actual Arrays (Array1): ", array1)
# Addition with Scalar Value
print("Addition : ", (5 + array1))

# Subtraction with Scalar Value
print("Subtraction : ", (5 - array1))

# Multiplication with Scalar Value
print("Multiplication : ", (5 * array1))

# Division with Scalar Value
print("Division : ", (array1 / 5))


arr = np.arange(0, 5)
print("Actual Array : ", arr)
# Square root
print("Square Root : ", np.sqrt(arr))
# max and min values
print("Max : ", np.max(arr))
print("Min : ", np.min(arr))
# Trigonometric functions, e.g. sin, cos, tan, arcsin, ......
print("Sin : ", np.sin(arr))
# Calculate the exponential (e^) of all elements in the input array
print("Exponential : ", np.exp(arr))
# log function
print("Log : ", np.log(arr))
# warning for inf

# Convert angles from degrees to radians
print("Degree to Radians : ", np.deg2rad(arr))

# Convert angles from radians to degrees
print("Radians to Degree : ", np.rad2deg(np.deg2rad(arr)))

array_2d = np.zeros((5, 5))  # Create a zero matrix
c = array_2d.shape[1]  # Using shape attribute, get the number to run the loop
