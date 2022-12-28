# lambda function is as inline function 
## when we need to pass function as an argument we use lambda function 

# normal function 
def func (a):
    return a+5

print(func(4))

## lambda function 
func2 = lambda a : a+5
print(func2(5))

square = lambda x : x*x
print(square(4))

# more parameter and default parameter is also possible
add = lambda a,  b, c =10 : a + b + c

print(add(2,3))