lis1 = ["hi", "my", "name", 78,  False]
#lis1 = {"hi" : "hello", "my":"manju", "name": "kkkk", 78: "xnjsxn",  False: 0}

##Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.

print(type(enumerate(lis1)))
# converting enumerate obj to List of tuples
print (list(enumerate(lis1)))

#we can change the starting index enumerate(itr, startIndex)
print (list(enumerate(lis1, 2)))

for item in enumerate(lis1):
    # print(index, item)
    print(item)

for index, item in enumerate(lis1):
    print(index, item)
