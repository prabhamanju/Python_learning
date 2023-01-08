import numpy as np

ar1 = np.arange(24)

print(ar1.shape)

b = ar1.reshape(4,3,2) # 24 = 2*12 or 2*3*4 or any factor of 24

print(b)