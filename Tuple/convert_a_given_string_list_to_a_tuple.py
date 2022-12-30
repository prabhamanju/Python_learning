str1 = "python     3.0 hello"

t1 = tuple(str1)

t2 = tuple(x for x in str1 if not x.isspace())

print(t1)
print(t2)
     
        
        