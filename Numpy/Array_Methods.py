import numpy as np
array_arange = np.arange(16)  # using arange()
array_randint = np.random.randint(0, 100, 10)  # using randint()

print('array using arange:', array_arange)
print('array using randint:', array_randint)

# any other num will give error, because we have 16
# elements in array_arange
print(array_arange.reshape(4, 4))

print("Maximum : ", array_randint.max())
print("Minimum : ", array_randint.min())

print("Maximum Index : ", array_randint.argmax())  # index starts from 0
print("Minimum Index : ", array_randint.argmin())  # index starts from 0
