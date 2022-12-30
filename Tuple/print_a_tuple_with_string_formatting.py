#Write a Python program to print a tuple with string formatting.

t = (100, 200, 300)
print(type(t))

#using str()
t1 = str(t)
print(t1)
print(type(t1))
    
#using format()
t_s = format(t)
print(t_s)
print(type(t_s))