# filter(function , list) create object for which function return true

li = [i for i in range(1, 100)]

no_div_by_5_list = list(filter(lambda a : a%5 == 0, li))

no_div_by_5_tuple = tuple(filter(lambda a : a%5 == 0, li))

print(no_div_by_5_list)    
print(no_div_by_5_tuple)    