tup1 = tuple("Hello World")

#get index of the first item whose value is passed as parameter
index = tup1.index("W")
print(index)

#define the index from which you want to search
index1 = tup1.index("W", 5)
print(index1)

#define the segment of the tuple to be searched
# index = tup1.index("e", 3, 6)
# print(index)

index = tup1.index("o", 3, 6)
print(index)