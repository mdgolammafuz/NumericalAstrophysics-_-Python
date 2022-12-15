import numpy as np

array_2d = np.ones((4, 4))
# Lets create a simple 1-D array and broadcast it to array_2d
print(array_2d + np.arange(0, 4))


array_1 = np.arange(1, 4)
array_2 = np.arange(1, 4)[:, np.newaxis]
# The official way of printing is used, format() and len() are used for revisions

print(array_1)
print("Shape of the array is: {}, this is {}-D array \n"
      .format(array_1.shape, len(array_1.shape)))
# (3,) indicates that this is a one-dimensional array (vector)

print(array_2)
print("Shape of the array is: {}, this is {}-D array"
      .format(array_2.shape, len(array_2.shape)))
# (3,) indicates that this is a one-dimensional array (vector)

# Broadcasting arrays
print(array_1 + array_2)

# Here is the practical example
print(np.array([1, 2, 3]) + np.array([1]))

# Here is the code for the above example!
print(np.ones([3, 3]) + np.array([1, 2, 3]))

# Code for the above visual broadcasting example.
print(np.ones([3, 1]) + np.arange(1, 4))
# using arange to revise the concept!
