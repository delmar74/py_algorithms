##############################
# Bubble sort
##############################

def bubble_sort2(list):
  m = 1
  loops = 0
  length = len(list)
  while m < length:
    for n in range(0,length-m):
      loops +=1
      if list[n] > list[n+1]:
        list[n],list[n+1] = list[n+1],list[n]
    m+=1

  print("Loops: ",loops)
  return list

i_list = [175, 48, 12, 25, 100, 10, 10, 40, 23, 17]
out = bubble_sort(i_list)

print(out)
