import numpy as np
# Original array
arr = np.array([0,1,2,3,4,5,6,7,8])
print(arr)

r1 = np.mean(arr)
print("\nMean: ", r1)

b = arr.reshape(3, 3)
print(b)

r2 = np.mean(b)
print("\nMean: ", r2)

r3 = np.std(b)
print("\nstd: ", r3)

r4 = np.var(b)
print("\nvariance: ", r4)
