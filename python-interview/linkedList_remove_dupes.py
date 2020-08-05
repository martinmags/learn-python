'''
Prompt: Write code to remove duplicates
from an unsorted linked list.

Extra:
How would you solve this problem if 
a temporary buffer is not allowed?
'''
from linked_list import Linked_List
from linked_list import Node

'''
Thought Process:
I would go about sorting it first if it was possible, so iterating
through duplicates would be easier(?)
'''
# Time Comp: O(n)
# Space Comp: O(n)
def remove_dupes(ll):
  output = set()
  curr = ll.head
  prev = Node(data=None, next_node=ll)
  while curr:
    # If not seen, add to set and continue iteration
    if curr.data not in output:
      output.add(curr.data)
      prev = curr
      curr = curr.next_node
    else:
      # Deletes by hopping over current node and continue iteration
      prev.next_node = curr.next_node
      curr.next_node = None
      curr = prev.next_node
  return ll

# Time Comp: O(n2)
# Space Comp: O(1)
def remove_dupes_1(ll):
  curr = ll.head
  while curr:
    runner = ll.head
    prev = ll.head
    while runner:
      if curr.data is runner.data:
        prev.next_node = runner.next_node
      else:
        prev = prev.next_node
      runner = runner.next_node
    curr = curr.next_node

L1 = Linked_List()
L1.insert(5)
L1.insert(3)
L1.insert(5)
L1.insert(5)
L1.insert(10)
L1.insert(5)
L1.insert(10)

L1.output()

print("Removing all duplicates...")
# remove_dupes(L1)
# remove_dupes_1(L1)
L1.output()