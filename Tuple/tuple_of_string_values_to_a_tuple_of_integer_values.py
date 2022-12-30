'''
Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))
'''

tup1 =(('333', '33'), ('1416', '55'))
print(type(tup1[0][0]))
# print(type(tup1[0][1]))
# print(tup1[0][0])
# print(tup1[0][1])

# print(tup1[1][0])
# print(tup1[1][1])
def tuple_int_str(tuple_str):
    for x in tuple_str:
        t = tuple((int(x[0]), int(x[1])))
        return t

tuple_str =  (('333', '33'), ('1416', '55'))      
print(tuple_int_str(tuple_str))