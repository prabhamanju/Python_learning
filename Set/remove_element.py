n = int(input())
s = set(map(int, input().split()))

print(len(s))

no_com = int(input())
for i in range(no_com):
    commad = input().split()
    print(commad)

    if commad[0] == 'pop':
        if len(s) > 0:
            s.pop()
            print(s)
        else:
            print(s)
            pass
    elif commad[0] == 'discard':
        s.discard(int(commad[1]))
        print(s)
    elif commad[0] == 'remove':
        if len(s) > 0:
            s.remove(int(commad[1]))
            print(s)
        else: 
            print(s)

print(sum(s))