"""
Task
You have a non-empty set s , and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format
The first line contains integer n , the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format
Print the sum of the elements of set  on a single line.
"""
n = int(input())
s = set(map(int, input().split()))

no_com = int(input())
for i in range(no_com):
    commad = list(input().split())
    if commad[0] == 'pop':
        if len(s) > 0:
            s.pop()
        else:
            pass
    if commad[0] == 'discard':
        s.discard(int(commad[1]))
    if commad[0] == 'remove':
        if len(s) > 0:
            s.remove(int(commad[1]))
        else: pass
print(sum(s))