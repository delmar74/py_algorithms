##############################
# Bubble sort
# Type: linear
#
# Time: O(n^2)
# Space: O(1)
##############################
import random

def bubble_sort(list):
  length = len(list);
  loops = 0

  for m in range(0, length-1):
    for n in range(0, length-1-m):  # optimozation: length-1 -> length-1-m, bec$
      if (list[n] > list[n+1]):
        list[n], list[n+1] = list[n+1], list[n]

  return list

# Random list
l = random.sample(range(1,100),10)
print(l)

result = bubble_sort(l)
print(result)
