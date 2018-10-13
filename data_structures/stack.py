##############################
# DS: Stack
#
# LIFO (last-in first-out)
#
# Operations:
# - PUSH(item) - add item to the top (rear), Return: nothing
# - POP() - removes the top (rear) item. Return: item
# - PEEK() - returns the top item from the stack but does not remove it
##############################
class Stack: 
  def __init__(self): 
    self.items = [] 

  def is_empty(self): 
    return self.items == [] 

  def push(self, item): 
    self.items.append(item) 

  def pop(self): 
    return self.items.pop() 

  def peek(self): 
    return self.items[len(self.items)-1] 

  def size(self): 
    return len(self.items)

s = Stack()

print('is_empty? '+str(s.is_empty()))
s.push('one')
s.push('two')
s.push('free')
s.push('four')
s.push('five')

print(s.items)

#print(s.size())
print(s.pop())
print(s.pop())

print(s.items)
