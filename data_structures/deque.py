##############################
# DS: Deque
#
# FIFO + LIFO 
#
# Operations:
# - ADD_FRONT(item) - add new item to the front. Return: nothing
# - ADD_REAR(item) - adds a new item to the rear. Return: nothing
# - REMOVE_FRONT() - removes the front item. Return: item
# - REMOVE_REAR() - removes the rear item. Return: item
##############################

class Deque: 
  def __init__(self): 
    self.items = [] 

  def is_empty(self): 
    return self.items == [] 

  def add_front(self, item):
    self.items.append(item) 

  def add_rear(self, item): 
    self.items.insert(0,item) 

  def remove_front(self): 
    return self.items.pop() 

  def remove_rear(self): 
    return self.items.pop(0) 
  
  def size(self): 
    return len(self.items)

d = Deque()

d.add_front('five')
d.add_front('three')
d.add_rear('ten')
d.add_rear('twelve')
d.add_front('one')

print(d.items)

d.remove_rear()
d.remove_rear()

print(d.items)

d.remove_front()

print(d.items)

