##############################
# Selection sort
# Type: linear
#
# Time: O(n^2)
# Space: O(1)
##############################
import random

def selection_sort(list):
    min = 0
    n = len(list)

    while(min <= n-1):
      temp = min
      while(temp <= n-1):      #finding minimum
        if (list[temp] < list[min]):
          list[min],list[temp] = list[temp],list[min]   #swapping element at start index with minimum
        temp = temp+1

      min = min+1
    return list

# Random list
l = random.sample(range(1,100),10)
print(l)

print(selection_sort(l))
