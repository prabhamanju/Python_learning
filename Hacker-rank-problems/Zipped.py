# Enter your code here. Read input from STDIN. Print output to STDOUT
#N = no_of_students in  X = no_of_subjects
N, X = list(map(int,input().split()))

#print(N , X)
subjects =[]
for i in range(X):
    subjects.append(list(map(float,input().split())))
    #print(subjects)
sub = zip(*subjects)
#print(list(sub))
for i in sub:
    print(sum(i)/X)
