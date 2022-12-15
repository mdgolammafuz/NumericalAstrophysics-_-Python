import numpy as np
array_arange = np.arange(16)  # using arange()
array_randint = np.random.randint(0, 100, 10)  # using randint()

print("Initial array :", array_arange)
# Let's take vector array, array_arange
print("Shape : ", array_arange.shape)
# As from its name, size of an array
print("Size : ", array_arange.size)
# type attribute returns the type of the data in the array.
print("Type : ", array_arange.dtype)
# Notice the two sets of brackets in the output,
# we are using reshape() to convert 1-D array to 2-D array/matrix
print("Reshaped : ", array_arange.reshape(4, 4))
print("New shape : ", array_arange.reshape(4, 4).shape)

print("Second shape : ",  array_arange.reshape(16, 1))
print("Second New shape : ",  array_arange.reshape(16, 1).shape)

print("Third shape : ",  array_arange.reshape(1, 16))
print("Third New shape : ",  array_arange.reshape(1, 16).shape)

# What is the data type of the object in the array?
print("Data Type : ", array_arange.dtype)
