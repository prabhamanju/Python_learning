# if __name__ == '__main__':
def runnerUp(arr):
    list1 = list(set(arr))
    a = max(list1)
    list1.remove(a)
    b = max(list1)
    print(b)
    
    
runnerUp([2,3,6,7,6,5,8])