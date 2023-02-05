'''
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Sample Input 0
3 # the number of students' records
Krishna 67 68 69 # name marks
Arjun 70 98 63
Malika 52 56 60
Malika      # query_name ## find avg of marks of malika

'''

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    # print(name)
    # print(line)
    score = list(map(float, line))
    # print(marks)
    student_marks[name] = score
quary_name = input()

marks = student_marks[quary_name]
print(marks)

avg = sum(marks)/n

print(avg)



