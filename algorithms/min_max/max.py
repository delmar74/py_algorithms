##############################
# Search max in list
##############################
import random

def max(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max


l = random.sample(range(1,100),10)

print(l)
print(max(l))
