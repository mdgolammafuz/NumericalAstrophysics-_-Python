import numpy as np
# Lets create a 2D martix with ones
array_2d = np.ones((4, 4))

print("2D Array")
print(array_2d)

# Lets broadcast 300 to the first row of array_2d
array_2d[0] = 300
print("\n After Broadcasting")
print(array_2d)

x = np.array([[1, 2], [3, 4]])

print(x)
