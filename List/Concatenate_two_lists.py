'''
Concatenate two lists in the following order
given 
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = []
for i in list1:
    for j in list2:
       list3.append(i + j)

print(list3, "\n")


# other method
new_list = [i + j for i in list1 for j in list2]
print(new_list)