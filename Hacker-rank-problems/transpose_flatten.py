"""
Task
You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Output Format
First, print the transpose array and then print the flatten.
"""

import numpy as np
n = input().split()
N = n[0]
M = n[1]
# print(n)
matrix = []
for i in range(int(N)):
    matrix.append(list(map(int,input().split())))
  
arr = np.array(matrix)
tranpose_arr = np.transpose(arr)
flattened_arr = arr.flatten()
# print(matrix )
print(tranpose_arr)
print(flattened_arr)