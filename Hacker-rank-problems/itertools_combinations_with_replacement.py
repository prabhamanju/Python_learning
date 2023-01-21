'''
itertools.combinations_with_replacement(iterable, r)
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
'''
'''
Task: You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format: A single line containing the string S and integer value k separated by a space.
Constraints: 0<k<=len(S) , The string contains only UPPERCASE characters.

Output Format:Print the combinations with their replacements of string S on separate lines.
S = HACK 2

Sample Output:
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''

from itertools import combinations_with_replacement

s = input().split()
string = sorted(s[0].upper())

print(string)
length = int(s[1])

comb = (list(combinations_with_replacement(string, length)))

for i in comb:
   print(''.join(i))
