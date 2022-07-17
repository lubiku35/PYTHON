

print("Welcome to the game!")
print("GAME OF CHOOSE")
print("")

user_name = input("Start by entering your name \n-> ")
user_age = int(input("Enter your age \n-> "))

if user_age < 18:
   print("Your age is not acceptable to play this game :(")
else:
   print(f"Welcome {user_name}")

print("Now i will explain you the rules: \nYou have 3 lives and after every bad decesion your life goes -1\nIf your lifes hits 0 its GAME OVER")

user_lifes = 3

while user_lifes != 0:
   print("")
   print("??? First question ???")
   print("How many states are in USA?\n 1: 15\n 2: 25\n 3: 50")
   us_states_input = int(input("Answer: "))
   if us_states_input == 1 or us_states_input == 15:
      print("Wrong answer")
      user_lifes -= 1
      print(f"Your lives are {user_lifes}")
   elif us_states_input == 2 or us_states_input == 25:
      print("Wrong answer")
      user_lifes -= 1
      print(f"Your lives are {user_lifes}")
   elif us_states_input == 3 or us_states_input == 50:
      print("Right answer")
      print(f"Your lives are {user_lifes}")

   print("")
   print("??? Second question ???")
   print("Choose left or right door\n 1: left\n 2: right")
   door_states_input = input("Answer: ")
   if door_states_input == "1" or door_states_input.lower() == "left":
      print("Right answer")
      print(f"Your lives are {user_lifes}")
   elif door_states_input == "2" or door_states_input.lower() == "right":
      print("Wrong answer")
      user_lifes -= 1
      print(f"Your lives are {user_lifes}")
   else:
      print("Invalid answer")
      user_lifes -= 1
      print(f"Your lives are {user_lifes}")

   print("")
   print("??? Third question ???")
   print("Whats authors favourite number?\n 1: 35\n 2: 11\n 3: 26")
   fav_states_input = int(input("Answer: "))
   if fav_states_input == 1 or fav_states_input == 35:
      print("Right answer")
      print(f"Your lives are {user_lifes}")
   elif fav_states_input == 2 or fav_states_input == 11:
      print("Wrong answer")
      user_lifes -= 1
      print(f"Your lives are {user_lifes}")
   elif fav_states_input == 3 or fav_states_input == 26:
      print("Wrong answer")
      user_lifes -= 1
      print(f"Your lives are {user_lifes}")
      
   if user_lifes == 0:
      print("You LOST :(")
      break
   else:
      print("You WON !!!")
      break 