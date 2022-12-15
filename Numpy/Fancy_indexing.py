import numpy as np

array_2d = np.zeros((5, 5))  # Create a zero matrix
array_2d.shape[1]  # Using shape attribute, get the number to run the loop
for i in range(array_2d.shape[1]):  # Using range() in the loop
    array_2d[i] = i
print(array_2d)  # Print/output the matrix

print(array_2d[[1, 2, 3]])
# We can use any order e.g., row 3, 0 and 4 in this case
print(array_2d[[3, 0, 4]])

# creating an array using arange()
array_2d = np.arange(24)

# converting a 1-D array using shape attribute into 2-D array
array_2d.shape = (6, 4)

# see what our 2-D array looks like!
print(array_2d)
print("\n ----------------------- \n")
# grabbing rows
# need to pass the list of required rows in square brackets
print(array_2d[[2, 4]])

# grabbing columns - notice the order in [3,2]
# print( array_2d[:,[3,2]] )
# [: for all_rows, [3,2] for 3rd and 2nd column]
