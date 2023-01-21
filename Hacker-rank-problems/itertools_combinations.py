"""itertools.combinations(iterable, r)

This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
"""

from itertools import combinations

print (*(combinations('12345',2)))

A = [1,1,3,3,3]
print (list(combinations(A,4)))

#######################################
"""
Task: You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format: A single line containing the string S and integer value k separated by a space.

Constraints: 0 < k <= len(S)

Output Format: Print the different combinations of string  on separate lines.

"""

s = input().split()
string = sorted(s[0])
length = int(s[1])

for i in range(1,length+1):
    comb = list(combinations(string, i))
    for val in comb:
        print("".join(val))