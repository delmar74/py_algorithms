##############################
# Insertion Sort
##############################

def insertion_sort(list):
  length = len(list)
  for i in range(1, length):
    current = list[i]
    position = i
    while(position > 0 and current<list[position-1]):
      list[position]=list[position-1]
      position -= 1
      print(str(list))
    list[position]=current
    print(str(position)+" >> "+str(current))
    print(str(list))

  return list

out_list = [12, 17, 4, 3,3,3, 10, 20, 15, 1, 8, 6]

print(out_list)
print(insertion_sort(out_list))
