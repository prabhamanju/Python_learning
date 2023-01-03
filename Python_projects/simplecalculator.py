def add(a,b):
    x = a+b
    print("addition of given and numbers : ", (x))

def sub(a,b):
    print("subtraction of given numbers : ", (a-b))

def mul(a,b):
    print("multiplication of given numbers : ", (a*b))
    

def div(a,b):
    print("multiplication of given numbers : ", (a/b))

print("---------for calculation-----------")

while True:
    print("A for addition")
    print("B for subtraction")
    print("C for multiplication")
    print("D for division")
    print("E for exit")

    choice = input("Please choose one option to perform operation : ")

    if choice == "E" or choice =="e":
        print("you entered E")
        quit()
    else:
        a=int(input("enter first number: "))
        b=int(input("enter first number: "))

        if choice == "A" or choice =="a":
        
            print("addition of given numbers : ")
            add(a,b)

        elif choice == "B" or choice =="b":
            print("addition of given numbers : ")
            sub(a,b)

        elif choice == "C" or choice =="c":
            print("multiplication of given numbers : ")
            mul(a,b)

        elif choice == "D" or choice =="d":
            print("division of given numbers : ")
            div(a,b)
    



