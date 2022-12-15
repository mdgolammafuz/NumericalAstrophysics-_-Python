import numpy as np
# Let's create an array using arange()
array_1d = np.arange(0, 10)
print("Original Array : ", array_1d)
array_1d[0:5] = 500
print("After Broadcasting : ", array_1d)
