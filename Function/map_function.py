# map(function, list) return an object.print
# map() applies given function on all items of list
# given function can be lambda function too


def square(num):
    return num * num

l1 = [1,4,6]
l2 = []
for item in l1:
    l2.append(square(item))

print(l2)


## using map()
l3 = map(square, l1) ## return an object 
l3 = list(l3) ## type case into list
print(l3)
