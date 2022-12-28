'''
Write a program to create a new string made of an input string’s first, middle, and last character.

'''

str1= "manju"

first_char = str1[0]

size_of_string = len(str1)
# Get middle index number
middle_index = int(size_of_string/2)

middle_char = str1[middle_index]

last_char = str1[size_of_string - 1]

print(first_char + middle_char + last_char )