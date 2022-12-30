# def mul1(a,b,*argv):
#     mul = a*b
#     for i in argv:
#         mul *=i
#     return mul

# print(mul1(1,2,3,4,5,6))

# def fun(**kwargs):
#     for key, value in kwargs.items():
#         print(key +":"+ str(value) )

# fun(arg1 = 1, arg2 = 2, arg3 =3)
##_____________________________________________________________________________##
import sys
from copy import copy, deepcopy
L1 = [1,2,[3,5],4]
L2 = copy(L1)
# L1[3] = 7
# print(L2)
L1[2].append(6)
print(L2)
print(L1)

# L1 = [1,2,[3,5],4]
# L2 = deepcopy(L1)
# # L2[3] = 8
# L2[2].append(6)
# print(L2)
# print(L1)

# if L1 is L2:
#     print("True")

# if L1 == L2:
#     print("True")

# x =5 
# y = copy(5)
# y = 6
# print(y)
# print(x)


# print(id(L1))
# print(id(L2))


