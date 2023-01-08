#Write a NumPy program to test element-wise for NaN of a given array.

import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array", a)
print("Test element-wise for NaN:")
print(np.isnan(a)) #isnan () function tests element-wise whether it is NaN or not and returns the result as a boolean array

print("Test element-wise for positive or negative infinity:")
print(np.isinf(a)) # The np.isinf () is a numpy library function used to test element-wise for positive or negative infinity.