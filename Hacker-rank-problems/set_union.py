"""
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
"""

n_e = int(input())
r_e = input().split(' ')
n_f = int(input())
r_f = input().split(' ')
# print(r_e)
c_s = set(r_e).union(set(r_f))
print(len(c_s))