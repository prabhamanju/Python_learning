# reduce() applies a rolling computation to sequential pair of element and return the final value

from functools import reduce
l1 = [2, 8, 40, 10, 29, 3]

a = reduce(max, l1)

print(a)