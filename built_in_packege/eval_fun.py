"""
The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression.
The expression can be a Python statement, or a code object.
"""

x = eval("9 + 5")
print(x)

"""
eval() can also be used to work with Python keywords or defined functions and variables. 
These would normally be stored as strings.
"""
y = type(eval("len"))
print(y) #<class 'builtin_function_or_method'>

z = type("len")
print(z)
