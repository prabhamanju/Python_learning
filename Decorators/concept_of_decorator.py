def find_div(a, b):
    print(a//b)
def new_div(func):
    print("before function call")
    def inner(a,b):
        if a < b:
            a, b = b, a
            func(a, b)
        elif a >b:
            func(a,b)
    print("after function call")
    return inner

div1= new_div(find_div)

div1(2, 8)
div1(4,2)
