# Author: Lubiku
# Bubble Sort

my_list = [3, 4, 5, 2, 6, 1, 7, 9, 8]

def bubbleSort(list):
   for i in range(len(my_list)):
      for j in range(len(my_list) - 1, i, -1):
         if list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]
   return list

print(bubbleSort(my_list))