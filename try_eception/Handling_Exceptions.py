T = int(input())
n = [input().split() for _ in range(T)]

for a,b in n:
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print('Error Code:' , e)
    except ValueError as ve:
        print('Error Code:', ve)


'''
input:
3
1 0
2 $
3 1
Output:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
'''