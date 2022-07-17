# Author: Lubiku
# Selection Sort 

my_list = [3, 4, 5, 2, 6, 1, 7, 9, 8]

def selectionSort(list):
   for item in range(len(list) - 1):
      minimum = item
      for i in range(item + 1, len(list)):   
         if (list[i] < list[minimum]):
            minimum = i
      if (minimum != i):
         list[item], list[minimum] = list[minimum], list[i]
   return list

print(selectionSort(my_list))   
             

             