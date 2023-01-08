import numpy as np

a = np.array([1,2,3])

b = np.repeat(a,3)

print(b)

a = np.array([[1,2,3]])
c = np.repeat(a,3, axis =1 ) # [[1 1 1 2 2 2 3 3 3]]
print(c)

d = np.repeat(a,3, axis =0 )   # [[1 2 3][1 2 3][1 2 3]]
print(d)