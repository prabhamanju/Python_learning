"""
Given the names and grades for each student in a class of N students, store them in a nested list and 
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
print each name on a new line.
"""
students=[]
marks = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    marks.append(score)
    sorted_marks = sorted(set(marks))
print(sorted_marks)
second_lowest_grade = sorted_marks[1]
students_list = []
for val in students:
    if second_lowest_grade == val[1]:
        students_list.append(val[0])
students_list.sort()
for name in students_list:
    print(students_list)

    # print(val[1], students)