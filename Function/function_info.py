def greeting ():
    print("Hello")

greeting()


def greetings(name):
    print("Hello " + name)

greetings("manju")


def sum(num1, num2):
    print(num1 + num2)
sum(2,4)


def Sum(num1, num2, num3):
    return (num1 + num2 + num3)
total = Sum(10, 20, 30)
print(total)


#function with list
#1)
def display_program(movies):
  print(f"Airing tonight : {movies}")

movies = ["Alien", "moon"]
display_program(movies)

#getting the number of passengers with len()
#2)

def count_passengers(passengers):
  print(len(passengers))

passengers = ["Sam", "Lee", "Sona", "Micale"]
count_passengers(passengers)


def is_booked(passengers):
  if len(passengers) > 4:
   print("booked")
  else:
    print("available")

passengers = ["Sam", "Lee", "Sona", "micale", "joe"]
is_booked(passengers)   



# Retrieve certain elements of List
def get_winner(top_player):
  winner = top_player[1]
  print(f"winner of the game is : {winner}")
  
top_player = ["jay", "Meg", "sasa"]


get_winner(top_player)


# Update top player list 

def update_top_player(top_player, change_player):
  top_player[0] = change_player  
  return top_player

update_top_player(top_player, "Lena")
print(top_player)


  
