name = input("enter your name: \n")
marks = input("enter your marks: \n")
phoneNo = input("enter your Phone number : \n")


template ="The name of the student is {}, his marks are {} and phone number is {}"

sent = template.format(name, marks, phoneNo)

print(sent)