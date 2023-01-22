"""Task
Read in two integers, a and , b and print three lines.
The first line is the integer division  a//b (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%b .
The third line prints the divmod of a and b.

Input Format: The first line contains the first integer,a , and the second line contains the second integer,b .
177
10

Output Format
Print the result as:
17
7
(17, 7)

"""
a = int(input())
b = int(input())

x = a//b
r = a%b
print(x)
print(r)
print(divmod(a,b))