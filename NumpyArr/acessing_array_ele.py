import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a.shape)
print(a)

# get specific element at [r,c]
#accessing 13 
print(a[1,5])

print(a[1,-2])

# get specific row
print(a[0, :])
print(a[1, :])

# get specific column
print(a[:,3])

# specific row with specific elements
print(a[0, 1:6:2])
print(a[0, 1:-1:2])

#access specific element and change it

a[1, 2] =20
print(a)
a[0, 2] =20
print(a)

#access specific element column wise and change it
a[ :, 2] = 5

print(a)

a[ :, 2] = [7,8]

print(a)