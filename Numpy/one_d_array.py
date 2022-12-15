import numpy as np
# Let's create a simple 1-D NumPy array.
# (we can use arange() as well.)
array_1d = np.array([-10, -2, 0, 2, 17, 106, 200])
# Getting value at certain index
print('The value at index 0:', array_1d[0])
# Using -ve index
print('The value at index -2: ', array_1d[-2])

print('Our original array is: ', array_1d)
print('Selected slice of the array is: ', array_1d[0:3])

# Using -ve index for index range
print('Our original array is: ', array_1d)
print('The values from 1:-2 index range are: ', array_1d[1:-2])

print('Value in array_1d upto index 2 : ', array_1d[:2])
print('Value in array_1d from index 2 : ', array_1d[2:])

print('Our original array is: ', array_1d)
# assigning new value at index 0 array_1d
array_1d[0] = -102
# let's check what is at index 0 now!
print('Our Updated array is: ', array_1d)

print('size of array_1D is: ',  array_1d.size)
print('305 % array_1d.size is (index location): ', 305 % array_1d.size)
print('value at the given index location: ', array_1d[305 % array_1d.size])
