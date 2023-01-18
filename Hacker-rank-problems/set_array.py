def average(array):
    array_set = set(array)
    print (array_set)
    total_height =  sum (array_set)
    print(total_height)
    total_no_distinct_height =  len(array_set)
    avg = float(total_height/total_no_distinct_height)
    avg = format(avg, '.3f')
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
# average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])
