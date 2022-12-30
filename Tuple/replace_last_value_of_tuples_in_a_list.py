#Write a Python program to replace last value of tuples in a list.
# Output [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for t in l:
    print(t)
    print(t[:2] + (100,))