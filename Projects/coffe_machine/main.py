"""
   Coffe Machine
   Author: Lubiku
"""

from source_data import MENU
from source_data import resources

# === Main Settings ===

expresso_price = MENU["expresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# === Functions === 

def report(data):
   print(f"Water: {data['water']}\nMilk: {data['milk']}\nCoffee: {data['coffee']}")

def coins():
   print("Please insert coins (1, 2, 5, 10, 20, 50)$")

   coin_1 = int(input("How many 1$? :")) * 1
   coin_2 = int(input("How many 2$? :")) * 2
   coin_5 = int(input("How many 5$? :")) * 5
   coin_10 = int(input("How many 10$? :")) * 10 
   coin_20 = int(input("How many 20$? :")) * 20
   coin_50 = int(input("How many 50$? :")) * 50
   amount = coin_1 + coin_2 + coin_5 + coin_10 + coin_20 + coin_50

   print(f"You inserted {amount}$")
   return amount

def calculateChange(user_sum_coins, price):
   change = user_sum_coins - price
   please_insert = price - user_sum_coins
   if change >= 0:
      print("Your drink is in making...")
      if change > 0:
         print(f"Your change {change}$")
   else:
      print(f"Ooops, lack of money. Please insert {please_insert}$ to validate")

def fillInIngredience():
   return resources

def calculateIngredients(drink_name):
   if drink_name == "expresso":
      consuptionIngredients(drink_name, rest_of_ingredience)
   elif drink_name == "latte":
      consuptionIngredients(drink_name, rest_of_ingredience)
   elif drink_name == "cappuccino":
      consuptionIngredients(drink_name, rest_of_ingredience)


def ingredientsChecker(in_water, in_milk, in_coffee):
   if in_water <= 0:
      print("Not available, lack of water...")
      return False
   elif in_milk <= 0:
      print("Not available, lack of milk...")
      return False
   elif in_coffee <= 0:
      print("Not available, lack of coffe...")
      return False
   else:
      print("Ingredients are available")
      return True

       
def consuptionIngredients(name_of_drink, ingredience):
   ingredience["water"] =  ingredience["water"] - MENU[name_of_drink]["ingredients"]["water"]
   ingredience["milk"] =  ingredience["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
   ingredience["coffee"] =  ingredience["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
   print(f"Remain ingredients: {ingredience}")         


# === CoffeMachine Code ===

# Load resources
rest_of_ingredience = fillInIngredience()

lets_continue = True

while(lets_continue):
   # User choice
   user_choice = input("Make your choice: \nExpresso\nLatte\nCappuccino\n->")

   # Calculate how much ingredience remain
   calculateIngredients(user_choice)

   # Check if we have enough ingredients
   if user_choice != "report":
      lets_continue = ingredientsChecker(rest_of_ingredience["water"],rest_of_ingredience["milk"],rest_of_ingredience["coffee"])

   # Can we continue
   if lets_continue == False:
      break

   # Control Report
   if user_choice.lower() == "report":
      report(rest_of_ingredience)

   # Main-Code Machine
   if user_choice.lower() == "expresso":
      print(f"Price of expresso: {expresso_price}$")
      sum = coins()
      calculateChange(sum, expresso_price)

   elif user_choice.lower() == "latte":
      print(f"Price of latte: {latte_price}$")
      sum = coins()
      calculateChange(sum, latte_price)

   elif user_choice.lower() == "cappuccino":
      print(f"Price of cappuccino: {cappuccino_price}$")
      sum = coins()
      calculateChange(sum, cappuccino_price)
   else:
      print("Wrong Choice") 