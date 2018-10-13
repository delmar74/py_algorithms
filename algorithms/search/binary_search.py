##############################
# SEARCH
# Binary Search
#
# Requirements:
# - ordered list
#
# Algorithm: 50/50 and so on
#
##############################

import random 

def bin_search(list, x):
    lower_bound = 0
    upper_bound = len(list)
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2    
        if x == list[compared_value]:
            return compared_value
        elif x < list[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None  

# Random list
x = 10
l = random.sample(range(1,20),12)

print(str(l) +', ' + str(x))

print(bin_search(l, x))
