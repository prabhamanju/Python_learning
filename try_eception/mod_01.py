def greet(name):
    print(f"Good Morning {name}")

# __name__ evaluate the name of the module in python from where the program is running
#print(__name__)
if __name__ == "__main__":
    name = input("enter your name : \n")
    greet(name)

#print(word)