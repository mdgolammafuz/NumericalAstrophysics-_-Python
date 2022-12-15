import numpy as np


def getArray():
   # Generating vector array
    vector_array = np.arange(25)
    # reshape to convert into 2-d
    matrix_array = vector_array.reshape(5, 5)
    # Scalar addition to the NumPy array
    return (matrix_array + 100)


print(getArray())
