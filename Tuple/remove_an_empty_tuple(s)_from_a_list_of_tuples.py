# Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''

l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l1 =[]
for t in l:
    if t != ():
        l1.append(t)

print(l1)


#other way 

l = [t for t in l if t]
print(l)