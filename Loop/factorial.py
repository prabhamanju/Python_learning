num = int(input("enter number: "))

# num! = 1 X 2 X 3.....X num

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print(f"factorial of given no : {factorial}")