##############################
# Search max in list
##############################
import random

def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


l = random.sample(range(1,100),10)

print(l)
print(max(l))
