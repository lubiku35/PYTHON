import random
from unittest import result
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

print("Password Generator")

num_letters = int(input("How many letters? \n"))
num_numbers = int(input("How many numbers? \n"))
num_special_char = int(input("How many special characters? \n"))

# letters, numbers, special characters which we will use

result = []

for item in range(0, num_letters):
   random_letter = random.randint(0, len(letters) - 1)
   result.append(letters[random_letter])

for item in range(0, num_numbers):
   random_number = random.randint(0, len(numbers) - 1)
   result.append(numbers[random_number])

for item in range(0, num_special_char):
   random_special_char = random.randint(0, len(special_char) - 1)
   result.append(special_char[random_special_char])

# randomize
# translator = ""
#
# for item in range(0, 10):
#    random_item_1 = random.randint(0, len(result) - 1)
#    random_item_2 = random.randint(0, len(result) - 1)
#
#    translator = result[random_item_1]
#    result[random_item_1] = result[random_item_2]
#    result[random_item_2] = translator

random.shuffle(result)
print(result)
 
    
# ["E", "a", "2", "5", "#"]


# from list to string
result_pass = ""

for item in result:
   result_pass += item 

print(result_pass)


