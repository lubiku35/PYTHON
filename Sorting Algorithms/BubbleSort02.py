# Author: Lubiku
# Bubble Sort

my_list = [3, 4, 5, 2, 6, 1, 7, 9, 8]

def bubbleSort(list):
   for i in range(len(my_list) - 1):
      for j in range(len(my_list) - 1):
         if my_list[j] > my_list[j + 1]:
            temp  = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(bubbleSort(my_list))