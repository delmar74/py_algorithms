##############################
# DS: Queue
#
# FIFO (first-in first-out)
#
# Operations:
# - ENQUEUE(item) - add new item to the rear. Return: nothing
# - DEQUEUE() - removes the front item. Return: item
##############################

class Queue: 
  def __init__(self): 
    self.items = [] 

  def is_empty(self): 
    return self.items == [] 

  def enqueue(self, item): 
    self.items.insert(0,item) 

  def dequeue(self): 
    return self.items.pop() 
  
  def size(self): 
    return len(self.items)


q = Queue()

q.enqueue('one')
print('Add item '+str(q.items[0]))

q.enqueue('two')
print('Add item '+str(q.items[0]))

q.enqueue('free')
print('Add item '+str(q.items[0]))

q.enqueue('four')
print('Add item '+str(q.items[0]))

q.enqueue('five')
print('Add item '+str(q.items[0]))

print(q.items)

print(q.dequeue())
print(q.dequeue())

print(q.items)
