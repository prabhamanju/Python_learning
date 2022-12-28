'''
Given string contains a combination of the lower and upper case letters.
Write a program to arrange the characters of a string so that all lowercase letters should come first.
'''

str1 = "manJUpra"

lower_case = []
upper_case = []
newStr1 = [] 

for char in str1:
    if char.islower():
        lower_case.append(char)
        print(lower_case)
    else:
        upper_case.append(char)

print(lower_case)
print(upper_case)

newStr1 = lower_case + upper_case
print(newStr1)

# join list
sorted_str = "".join(newStr1)

print(sorted_str)