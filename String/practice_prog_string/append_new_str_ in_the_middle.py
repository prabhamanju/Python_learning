'''
Given two strings, s1 and s2. Write a program to create a new string s3 by appending 
s2 in the middle of s1.
'''

s1 = "Ault"
s2 = "Kelly"

# middle index number of s1
mi = int(len(s1)/2)

# get character from 0 to the middle index number from s1
mid_char = s1[:mi]

# concatenate s2 to it
x = mid_char + s2

# append remaining character from s1
x = x + s1[mi:]
print(x)