# Author: Lubiku
# Bubble Sort

my_list = [3, 4, 5, 2, 6, 1, 7, 9, 8]

for i in range(len(my_list) - 1):
   for i in range(len(my_list) - 1):
      if my_list[i] > my_list[i + 1]:
         temp = my_list[i]    #temporálna premenná
         my_list[i] = my_list[i + 1]
         my_list[i + 1] = temp
      print(f'Index is: {i} -> {my_list}')

