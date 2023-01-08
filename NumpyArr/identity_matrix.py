#Write a NumPy program to create a 3x3 identity matrix.
'''
 An identity matrix is a given square matrix of any order which contains on its main diagonal 
 elements with value of one, while the rest of the matrix elements are equal to zero.

'''

import numpy as np
id_matrix = np.identity(5)
print('3x3 matrix:')
print(id_matrix)


