import numpy as np

a = np.array([1, 2, 3, 4, 5])
#b = a ## don't do this as when you want to change elements in b, a will get change accordingly
b = a.copy()
b[2] = 20

print(a)
print(b)