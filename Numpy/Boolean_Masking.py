import numpy as np


# Creating a simple array using arange()
array_1d = np.arange(1, 11)
print("Original Array : ", array_1d)

# lets create a bool_array for some condition, say array_1d > 3
bool_array = array_1d > 3
print("Is Greater than 3 Array : ", bool_array)

# A number is even, if number % 2 is 0
mod_2_mask_1d = 0 == array_1d % 2
print("IsEven Array : ", mod_2_mask_1d)
# filtering out the odds in masking operation
even_values = array_1d[mod_2_mask_1d]
print("Even Values : ", even_values)

# Let's check with our array_2d
array_2d = np.arange(24)
array_2d.shape = (6, 4)
mask_mod_2_2d = 0 == array_2d % 2  # masking
print(array_2d)
print(mask_mod_2_2d)

# filtering out the odd numbers in the masking operation
print(array_2d[mask_mod_2_2d])
