tup = (4, 6, 2, 8, 3, 1)

#tuples are immutable, so you can not add new elements but 
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tup1 = tup + (9,)
print(tup1)

#adding items in a specific index
tup2 = tup[:2] + (9,7)
print(tup2)

tup3 = tup[:2] + (9,7) + tup[2:]
print(tup3)

#converting the tuple to list
tup_lis = list(tup)
print(tup_lis)

tup_lis.append(0)
print(tup_lis)