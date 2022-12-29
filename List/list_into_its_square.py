'''
Given a list of numbers. write a program to turn every item of a list into its square.
'''

numbers = [1, 2, 3, 4, 5, 6, 7]

new_num = []
for i in numbers:
    new_num.append(i * i)

print(new_num)


#Use list comprehension

new_num = [i * i for i in numbers]
print(new_num)