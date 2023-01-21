"""
itertools.permutations(iterable[, r])

This tool returns successive r length permutations of elements in an iterable.

If r is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
"""

from itertools import permutations
print (*permutations(['1','2','3']))

print("all possible permutation with given length (2)")

print (list(permutations(['1','2','3'], 2)))

print("all possible permutations for string (abc)")

print (tuple(permutations('abc',3)))


"""Task

You are given a string S .
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format : A single line containing the space separated string S and the integer value k.
Output Format : Print the permutations of the string S on separate lines.
"""

S, k = input().split(" ")

print(*("".join(i) for i in list(permutations(sorted(S), int(k)))), sep = "\n")