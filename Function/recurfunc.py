## RECURSION : function call itself 

def recFun(num):
    if num == 1 or num == 0:
        return 1    
    return num * recFun(num -1)

print(recFun(5))