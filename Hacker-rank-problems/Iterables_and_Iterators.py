from itertools import combinations
N = int(input())
l = list(input().split())
print(l)
k = int(input())

comb = list(combinations(l, k))
print(comb)
count = 0
for i in comb:
    if 'a' in i:
        print([i])
        count= count+1
print(count)
print(count/len(comb))
