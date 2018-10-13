##########################
# Bubble sort
##########################

def bubble_sort(list):
  length = len(list);
  loops = 0

  for m in range(0, length-1):
    for n in range(0, length-1-m):  # optimozation: length-1 -> length-1-m, bec$
      if (list[n] > list[n+1]):
        list[n], list[n+1] = list[n+1], list[n]

  return list

i_list = [175, 48, 12, 25, 100, 10, 10, 40, 23, 17]
out = bubble_sort(i_list)

print(out)
