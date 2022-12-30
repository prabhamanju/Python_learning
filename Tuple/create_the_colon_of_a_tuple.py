#Write a Python program to create the colon of a tuple.
from copy import deepcopy

tup1 = ("HELLO", 5, [], True) 
tup2 = deepcopy(tup1)
print(type(tup2))
print(tup2)
tup2[2].append(50)
print(tup2)
print(tup1)