#Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

import numpy as np
array_0=np.zeros(10) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# array=np.zeros(10)
print("An array of 10 zeros:")
print(array_0)
print(array_0.size)
print(array_0.itemsize)


a = np.zeros((2,3))
print(a)
print(a.size)

# array_1=np.ones(10)
# print("An array of 10 ones:")
# print(array_1)

# array_5=np.ones(10)*5
# print("An array of 10 fives:")
# print(array_5)