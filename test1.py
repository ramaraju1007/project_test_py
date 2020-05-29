"""
Design a binary tree and then write an algorithm to print
the least(nearest) two common parent(if 2 parents exist
otherwise 1  common parent) node between 2 nodes
of a binary tree for given 2 key values which are present in binary tree.
"""
class Node:
  def __init__(self,val):
    self.val = val
    self.left_Node = None
    self.right_Node = None
    self.Parent = None

class BinaryTree:
  def __init__(self,val):
    self.root = Node(val)

def lowest_common_ancestor(node1,node2):
  ancestor_node1 = [] # use slice to store the ancestor of node1
  ancestor_node2 = [] # use slice to store the ancestor of node1
  curr = node1 
  while(curr!=None):
    curr = curr.Parent
    if(curr != None):
      ancestor_node1.append(curr.val) # add ancestors of node1
  curr = node2 
  while(curr!=None): 
    curr = curr.Parent
    if(curr != None):
      ancestor_node2.append(curr.val) # add ancestors of node2
  #print(ancestor_node1,ancestor_node2)
  for i in ancestor_node1:
      for j in ancestor_node2:
          if (i == j):
             #print("nodes ",i)
             print(i)
             break
      
def main():

  # create binarytree 2 as root
  BST = BinaryTree('2')
  #add nodes 1, 3, 4,5 and 6
  BST.root.left_Node = Node(1)
  BST.root.left_Node.Parent = BST.root
  BST.root.right_Node = Node(3)
  BST.root.right_Node.Parent = BST.root
  
  BST.root.right_Node.left_Node = Node(4)
  BST.root.right_Node.left_Node.Parent = BST.root.right_Node
  BST.root.right_Node.right_Node = Node(5)
  BST.root.right_Node.right_Node.Parent = BST.root.right_Node
  
  BST.root.right_Node.right_Node.left_Node = Node(6)
  BST.root.right_Node.right_Node.left_Node.Parent = BST.root.right_Node.right_Node
  # find least common parent, If nodes 1 and 5 are passed as parameters 
  lowest_common_ancestor(BST.root.left_Node,BST.root.right_Node.right_Node)

  print('\n')
  # find least common parent, If nodes 3 and 6 are passed as parameters
  lowest_common_ancestor(BST.root.right_Node,BST.root.right_Node.right_Node.left_Node)
  
  print('\n')
  # find least common parent, If nodes 4 and 6 are passed as parameters
  lowest_common_ancestor(BST.root.right_Node.left_Node,BST.root.right_Node.right_Node.left_Node)
  
if __name__ == "__main__":
  main()
