# WAP to print 4th, 5th, and 7th element from list using enumerator function()
l = [1,2,3,4,5,6,7,7,8]

for i, ele in enumerate(l):
    if i == 3 or i == 4 or i == 6:
        # print(i, ele)
        print(f"{i + 1}th element is {ele}")