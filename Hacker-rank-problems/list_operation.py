if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(0,N):
        comand = input().split(" ")
        print(comand)
        if comand[0] == 'insert':
            index = int(comand[1])
            val = int(comand[2])
            print(index, val)
            list.insert(index, val)
            print(list)
        elif comand[0] == 'print':
            print(list)
        elif comand[0] == 'remove':
            if int(comand[1]) in list:
                list.remove(int(comand[1]))
                print(list)
        elif comand[0] == 'append':
            list.append(int(comand[1]))
            print(list)
        elif comand[0] == 'sort':
            list.sort()
        elif comand[0] == 'pop':
            if len(list) > 0:
                list.pop()
        elif comand[0] == 'reverse':
            list.reverse()