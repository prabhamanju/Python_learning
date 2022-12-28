'''
Given a string s1, write a program to return the sum and average of the digits that appear in the string, 
ignoring all other characters.
'''
x = 0
cnt = 0
s1 = "hiiamdiital@#29222"
for char in s1:
    if char.isdigit():
        x = x+int(char)
        #print(char)
        cnt +=1
    
avg = x/cnt

print(f"sum : {x}")
print(f"average : {avg}")