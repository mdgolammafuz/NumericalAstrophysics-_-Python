import numpy as np
array_2d = np.arange(24)  # creating 1D array using arange()
array_2d.shape = (6, 4)  # converting into 2D
print(array_2d)  # How the 2D array look like!

# To get a complete row (row 3rd in this case, remember 0 is for row 1)
print(array_2d[2])

print(array_2d[-4])  # -0 and 0 is same index

print(array_2d[5, 2])

# another way
row = 5
column = 2
print(array_2d[row, column])

# Just to make sure, use [row][col] :)
print(array_2d[5][2])

# array_2d[:2,:2].shape gives (2,2),
# 4 elements for top left corner
# array_2d[0:2,0:2] is same as array_2d[:2,:2]
print(array_2d[:2, :2])

# getting inner slice
print(array_2d[2:4, 2:4])
