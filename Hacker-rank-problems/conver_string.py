'''
convert all lowercase letters to uppercase letters and vice versa.
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

'''

def swap_case(s):
    ans = list(s)
    print(ans)
    for i in range(len(ans)):
        if ans[i].islower():
            ans[i] = ans[i].upper()
        elif ans[i].isupper():
            ans[i]=ans[i].lower()
    return "".join(ans)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
