import random

randomNumber = random.randint(1, 100)

# print(randomNumber)

userNumber = None
guessed = 0

while(userNumber != randomNumber):
    userNumber = int(input("Enter any number between 1 to 100 : "))
    guessed += 1
    if userNumber == randomNumber:
        print("you guessed it correct")
    else:
        if userNumber > randomNumber:
            print("you guessed it wrong! Enter smaller number")
        elif userNumber < randomNumber:
            print("you guessed it wrong! Enter larger number")
    

print(f"how many time you guessed {guessed}")

# write guess in file if guess attempt is broken

with open ("high_score.txt") as f:
        high_score = int(f.read())

if guessed > high_score :
    print("you have just broken the high score")
    with open ("high_score.txt", "w") as f:
        f.write(str(guessed)) 
