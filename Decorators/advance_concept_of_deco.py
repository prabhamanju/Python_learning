def smart_div(func):
    print("execute" ,func.__name__, "function")
    def inner(a,b):
        if a < b:
            a, b = b, a
            func(a,b)
        elif a > b:
            func(a,b)

    return inner

@smart_div
def find_div(a, b):
    print(a//b)

find_div(4,2)
find_div(4,16)
