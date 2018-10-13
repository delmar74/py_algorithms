##############################
# RECURSION
# 
# sum(n) = 1+2+..+n
##############################

def sum(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return n+sum(n-1)

print(sum(5))

