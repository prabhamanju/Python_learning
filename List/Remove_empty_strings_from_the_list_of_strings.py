list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print("Original list is : " + str(list1))

while("" in list1):
    list1.remove("")

print("Modified list is : " + str(list1))
print("\n")

# using list comprehension
test_list = [i for i in list1 if i]
print("Modified list is : " + str(list1))


#Use a filter() function to remove the None / empty type from the list
#fastest way to perform this task

test_list = list(filter(None, list1))
print(test_list)
