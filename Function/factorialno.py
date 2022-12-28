# num ! = 1 * 2 * 3 * 4 * ..... * num
# num ! = num * (num-1)!

def factorial(num):
    fact = 1
    for i in range(num):
        fact = fact * (i+1)
    return fact

f = factorial(4)
print(f)