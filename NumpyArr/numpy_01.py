#Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np
x = np.array([1, 2, 3, 4])
print("Original array:",x)

print("Test if none of the elements of the given array is zero:")
print(np.all(x))

y = np.array([1, 0, 2, 3])
print("Original array:",y)

print("Test if none of the elements of the given array is zero:")
print(np.all(y))
