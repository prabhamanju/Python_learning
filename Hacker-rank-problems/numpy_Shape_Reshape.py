"""
shape
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
reshape
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not 
modify the original array itself.
"""
"""
Task
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
Input Format
A single line of input containing 9 space separated integers.
1 2 3 4 5 6 7 8 9
Output Format
Print the 3X3 NumPy array.
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
import numpy 
arr = input().split()
arr = numpy.array(arr,int)
changed_shape = numpy.reshape(arr,(3,3))
print(changed_shape)