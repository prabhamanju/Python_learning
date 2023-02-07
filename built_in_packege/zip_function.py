A = [1,2,3]
B = [6,5,4]
C = [7,8,9]


print(zip(A,B,C)) #<zip object at 0x0000020ADCE00080>

print(list(zip(A,B,C))) #[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

print(*zip(A,B,C)) #(1, 6, 7) (2, 5, 8) (3, 4, 9) 

y = zip(A,B,C)
for i in y:
    print(sum(i))