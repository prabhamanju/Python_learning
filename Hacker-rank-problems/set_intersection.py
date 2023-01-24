"""
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
"""


n_e = int(input())
r_e = input().split()

n_f = int(input())
r_f = input().split()

print(r_e)
print(r_f)
print((set(r_e)&(set(r_f))))
# Output the total number of students who have subscriptions to both English and French newspapers.
print(len(set(r_e).intersection(set(r_f))))
