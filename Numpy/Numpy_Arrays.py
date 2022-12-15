# A standard way of importing NumPy
import numpy as np
# Let's check numpy's version
# print( np.__version__ )

# Creating a Python list "my_list".
my_list = [-1, 0, 1]
# Well, it's a good idea to confirm items in "my_list" and its type!
print(my_list, type(my_list))

# Creating a Python list "my_list".
my_list = [-1, 0, 1]
# Creating a NumPy array from my_list
my_array = np.array(my_list)
print(my_array, type(my_array))

# Let's create and cast a list of list to generate 2-D array
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_matrix)
# Two-dimensional array from Matrix
matrix_one = np.array(my_matrix)
print(matrix_one)

# We can use Tuple instead of a list as well.
my_tuple = (-1, 0, 1)
my_array = np.array(my_tuple)
print(my_array, type(my_array))


# similar to range() in Python, up to but not including 10
print(np.arange(0, 10))

# We can give a step (2 in this case)
print(np.arange(0, 11, 2))

# We can give the step and dtype
print(np.arange(0, 10, 2, dtype=float))  # type: ignore


# start from 1 & end at 15 with 10 evenly spaced points b/w 1 to 15.
print(np.linspace(1, 15, 15))  # type: ignore

# Let's find the step size with "retstep" which returns the array and the step size
my_linspace = np.linspace(5, 15, 9, retstep=True)  # type: ignore
print(my_linspace)

# We can grab array and step size separately.
print('array is: ', my_linspace[0])
print('stepsize is: ', my_linspace[1])

# 1-D array
print(np.linspace(0, 15, 30))

# 1-D array with 3 elements (zeros)
print(np.zeros(3))

# Creating 2-D array, (no_row, no_col) passing a tuple
print(np.zeros((4, 6)))


# 1-D array with 3 elements (ones)
print(np.ones(3))

# Creating 2-D array, (no_row, no_col) passing a tuple
print(np.ones((4, 6)))

print(np.eye(5))


# 1-D array with three elements
print(np.random.rand(3))

# row, col, note we are not passing a tuple here
# each dimension (num_of_rows, num_of_columns) is a separate argument
print(np.random.rand(3, 2))


# 1-D array of two elements.
print(np.random.randn(2))

# 2-D array (4x4), 16 elements.
# no tuple, each dimension as a separate argument
print(np.random.randn(4, 4))


# returns one random int, 1 inclusive, 100 exclusive
print(np.random.randint(1, 100))

# returns ten random int,
print(np.random.randint(1, 100, 10))

print(np.arange(1, 7))      # Takes default steps of 1 and doesn't include 7
print(np.arange(5))     # Starts at 0 by defualt and ends at 4, giving 5 numbers
print(np.arange(1, 10, 3))      # Starts at 1 and ends at less than 10,
# with a step size of 3
