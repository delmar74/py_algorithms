##############################
# SEARCH
# Linear Search in unordered list
#
# Algorithm: ..
#
##############################
import random 

def sequential_search(list, item): 
  pos = 0 
  found = False 

  while pos < len(list) and not found: 

    print(str(pos)+': ' + str(item) + ' - ' + str(list[pos]))

    if list[pos] == item: 
      found = True 
    else: 
      pos = pos+1 
  return found

# Random list
l = random.sample(range(1,20),15)

# Value to search
x = 10 

print(len(l))

print(str(l) +', ' + str(x))
print(sequential_search(l,x))
