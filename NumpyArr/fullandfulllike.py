import numpy as np
#create array of given shape and fill with given value
a = np.full((2,3),99)
print(a)


#create array with some other existing array
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

b = np.full_like(a, 10)
print(b)

c = np.full(a.shape,20)
print(c)
