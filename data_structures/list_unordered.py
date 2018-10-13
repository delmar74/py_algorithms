##############################
# DS: Unordered List
#
# Operations:
# - APPEND(item) - adds a new item to the end of the list. RETURN: nothing
# - ADD(item) - add item to the list. RETURN: nothing
# - INSERT(pos,item) - adds a new item to the list at position pos. RETURN: nothing
# - REMOVE(item) - removes the item from the list. RETURN: nothing
# - POP() - removes and returns the last item in the list. RETURN: item
# - POP(pos) - removes and returns the item at position pos. RETURN: item
# - SEARCH(item) - searches for the item in the list. RETURN: True/False
# - INDEX(item) - returns the position of item in the list. RETURN: index
##############################

class Node:
   def __init__(self, init_data):
      self.data = init_data
      self.next = None

   def get_data(self):
      return self.data

   def get_next(self):
      return self.next
 
   def set_data(self, new_data):
      self.data = newdata

   def set_next(self, new_next):
      self.next = new_next

class UnorderedList:

   def __init__(self):
      self.head = None

   def is_empty(self):
      return self.head == None

   def add(self, item):
     temp = Node(item)
     temp.set_next(self.head)
     self.head = temp

   def size(self):
     current = self.head
     count = 0
     while current != None:
        count = count + 1
        current = current.get_next()
     return count

   def search(self,item):
     current = self.head
     found = False
     while current != None and not found:
        if current.get_data() == item:
           found = True
        else:
           current = current.get_next()
     return found

   def remove(self, item):
     current = self.head
     previous = None
     found = False
     while not found:
       if current.get_data() == item:
         found = True
       else: 
         previous = current
         current = current.get_next()
     if previous == None:
       self.head = current.get_next()
     else:
       previous.set_next(current.get_next())
