"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X, c)in the string.

Input Format: A single line of input consisting of the string S.

Output Format: A single line of output consisting of the modified string.

Constraints: All the characters of  denote integers between 0 and 9.

Sample Input: 1222311
Sample Output: (1, 1) (3, 2) (1, 3) (2, 1)

"""

from itertools import groupby

s = input()

x = groupby(s)

for key, grp in x:
    print ((len((list(grp))), int(key)), end = " ")