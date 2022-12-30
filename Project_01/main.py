import random

def winGame(comp_player, player):
    if comp_player == player:
        return None
    if comp_player == "r":
        if player == "p":
            return False
        elif player == "s":
            return True

    if comp_player == "p":
        if player == "r":
            return False
        elif player == "s":
            return True

    if comp_player == "s":
        if player == "r":
            return False
        elif player == "p":
            return True

comp_player = input("computer's turn rock(r) paper(p) seizer(s)")
player = input("player's turn select rock(r) paper(p) or seizer(s)")

randNo = random.randint(1,3)
if randNo ==1:
    comp_player ="r"
elif randNo ==2:
    comp_player =="p"
elif randNo ==3:
    comp_player =="s"

print(f"comp_player choose {comp_player}")
print(f"player choose {player}")
w = winGame(comp_player , player)

if w == None:
    print("tie")
elif w:
    print("you won")
else:
    print("you loose")