"""
Task
Dr. John Wesley has a spreadsheet containing a list of student's ,ID ,marks,class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.

Input Format
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the marks, ID's, name and class , under their respective column names.

5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Output Format
Print the average marks of the list corrected to 2 decimal places.

78.00


"""

total_students = int(input())
name_field = input().split()
students_list =[]
s = 0

for i in range(total_students):    
    students_list.append(input().split()) 
    
mark = name_field.index("MARKS")
    
#print(students_list)

for i in range(total_students):
    s += int(students_list[i][mark])
print(s/total_students)