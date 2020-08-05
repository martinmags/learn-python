'''
Singly Linked List
TIME-COMP
  Insert: O(n)
  Delete: O(n)
  Search: O(n)
  Output: O(n)
  Sort:
'''
class Node:
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

# Methods: Insert, Find, Delete
class Linked_List:
  def __init__(self, head=None):
    self.head = head

  def insert(self, data):
    new_node = Node(data)
    # If empty
    if self.head is None:
      self.head = new_node
      return
    # Iterate until found position to insert
    curr = self.head
    while curr:
      if curr.next_node is None:
        curr.next_node = new_node
        break
      else:
        curr = curr.next_node
  
  def size(self):
    curr = self.head
    count = 0
    # If empty
    if self.head is None:
      return count
    else:
      while curr:
        curr = curr.next_node
        count += 1
    return count    


  def search(self, data):
    curr = self.head
    is_found = False
    while curr:
      if curr.data is data:
        is_found = True
        break
      else:
        curr = curr.next_node
    return is_found


  def delete(self, data):
    curr = self.head
    prev = Node(data=None, next_node=self.head)
    while curr:
      if curr.data is data:
        prev.next_node = curr.next_node
        curr.next_node = None
        return
      else:
        prev = curr
        curr = curr.next_node
    return

  def output(self):
    curr = self.head
    print("Output: ", end='')
    while curr:
      print(curr.data, end=' ')
      curr = curr.next_node
    print()

  def sort(self):
    curr = self.head
    prev = None
    
# Tests
# L1 = Linked_List()
# L1.insert(3)
# L1.insert(5)
# L1.insert(8)
# L1.output()
# print("Size:", L1.size())
# print("Deleting:", 5)
# L1.delete(5)
# print("Deleting:", 10)
# L1.delete(10)
# L1.output()
# print("Searching for", 8)
# print(L1.search(8))
# print("Searching for", 2000)
# print(L1.search(2000))