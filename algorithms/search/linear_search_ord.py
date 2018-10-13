##############################
# SEARCH
# Linear Search in ordered list
#
# Algorithm: ..
#
##############################
import random 

def ordered_sequential_search(list, item): 
  pos = 0 
  found = False 
  stop = False

  while pos < len(list) and not found and not stop: 
    
    print(str(pos)+': ' + str(item) + ' - ' + str(list[pos]))

    if list[pos] == item: 
      found = True 
    else: 
      if list[pos] > item:
        stop = True
      else:
        pos = pos + 1 
  return found


# Random list
l = sorted(random.sample(range(1,20),15))

# Value to search
x = 10 

print(str(l) +', ' + str(x))
print(ordered_sequential_search(l,x))
