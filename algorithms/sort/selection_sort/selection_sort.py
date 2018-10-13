##############################
# Selection sort
##############################

def selection_sort(a_list):
  for fill_slot in range(len(a_list) - 1, 0, -1):

    print(fill_slot)

    pos_of_max = 0
    for location in range(1, fill_slot + 1):
      if a_list[location] > a_list[pos_of_max]:
        pos_of_max = location
    temp = a_list[fill_slot]
    a_list[fill_slot] = a_list[pos_of_max]
    a_list[pos_of_max] = temp
  return a_list

a = [10,50,25,30,4,8,35,35,28]
print(selection_sort(a))
