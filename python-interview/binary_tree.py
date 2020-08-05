
class Node:
  def __init__(self, data=None,left_node=None, right_node=None):
    self.left_node = left_node
    self.right_node = right_node
    self.data = data

class Binary_Tree:
  def __init__(self, root=None):
    self.root = Node(data=root)

  '''
  Time Comp:
  Space Comp:
  Root->Left->Right
    # Visit Node and print value
    # Traverse Left
    # Traverse Right
  '''
  def preorder_traversal(self, curr):
    if curr is None:
      return
    print(curr.data, end=' - ')
    self.preorder_traversal(curr.left_node)
    self.preorder_traversal(curr.right_node)

  '''
  Time Comp:
  Space Comp:
  Left->Root->Right
  '''
  def inorder_traversal(self, curr): 
    if curr is None:
      return
    self.inorder_traversal(curr.left_node)
    print(curr.data, end=' - ')
    self.inorder_traversal(curr.right_node)
  
  def inorder_traversal_stack(self, curr):
    stack = []
    stack.append(curr)
    while True:
      if curr is not None:
        stack.append(curr)
        curr = curr.left_node
      elif stack:
        curr = stack.pop()
        print(curr.data, end=" ")
        curr = curr.right_node
      else:
        break
    print()
      

# BFS
# while True:
#   if tracker:
#       curr = tracker.pop(0)
#   else: 
#       break
      
#   if curr:
#       print(curr.val)
#       tracker.append(curr.left)
#       tracker.append(curr.right)
#   else:
#       continue
      


  '''
  Time Comp: 
  Space Comp:
  Left->Right->Root
  '''
  def postorder_traversal(self, curr):
    if curr is None:
      return
    self.postorder_traversal(curr.left_node)
    self.postorder_traversal(curr.right_node)
    print(curr.data, end=' - ')




#     3
#   4   12
# 8 16  40  20
tree = Binary_Tree(3)
r = tree.root
child0 = tree.root.left_node = Node(data=4)
child1 = tree.root.right_node = Node(data=12)
child2 = tree.root.left_node.left_node = Node(data=8)
child3 = tree.root.left_node.right_node = Node(data=16)
child4 = tree.root.right_node.left_node = Node(data=40)
child5 = tree.root.right_node.right_node = Node(data=20)

tree.inorder_traversal_stack(r)


