# sum(N) = sum(N - 1) + N

def sumOfNaturalNo (n):
    if n <= 1:
        return 1
    else:
        return n + sumOfNaturalNo (n-1)

N = 5
print(sumOfNaturalNo(N))
    
