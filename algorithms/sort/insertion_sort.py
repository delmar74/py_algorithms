##############################
# Insertion Sort
# Type: linear
#
# Time: O(n^2)
# Space: O(1)
##############################
import random

def insertion_sort(list):
  length = len(list)
  for i in range(1, length):
    current = list[i]
    position = i
    while(position > 0 and current<list[position-1]):
      list[position]=list[position-1]
      position -= 1
      #print(str(list))
    list[position]=current
    #print(str(position)+" >> "+str(current))
    #print(str(list))

  return list

# Random list
l = random.sample(range(1,100),10)
print(l)

print(insertion_sort(l))
