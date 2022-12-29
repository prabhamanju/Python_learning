num = int(input("enter a number : \n"))
# table = []
# for i in range(1,11):
#     m = i * num
#     table.append(m)
# print(table)

table = [i*num for i in range(1,11)]
print(table)

# write this table into a file

with open("table.txt", "a") as f:
    f.write(str(table))
    f.write("\n")