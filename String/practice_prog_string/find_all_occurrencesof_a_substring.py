'''
Write a program to find all occurrences of “USA” in a given string ignoring the case.
'''

str1 = "Welcome to USA. usa Awesome, isn't it?"
#subStr = "USA"
temp = str1.lower()
print(temp)

count = temp.count("usa")

print(count)