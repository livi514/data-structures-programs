#Task: implement a binary tree with functions for insertion and inorder traversal.

#implement the tree as a list
tree = [null] #the first element will be Null, to make operations easier later

def add_node(node):
  '''
  Function for adding a new node to the tree.
  '''
  if len(tree) == 1: #this means there are no nodes in the tree. There is one element in the list as the first element is Null.
    tree.append(node)
  else:
    #add node somehow?
    for node in tree:
      #find a node with less than two children

def find_left_child(node):
  node_index = tree.index(node)
  left_child_index = node_index*2
  return tree[left_child_index]

def find_right_child(node):
  node_index = tree.index(node)
  right_child_index = node_index*2+1
  return tree[right_child_index]

def find_parent(node):
  node_index = tree.index(node)
  parent_index = node_index//2
  return tree[parent_index]

def find_root(node):
  return tree[1]

def is_node_leaf(node):
  node_index = tree.index(node)
  num_nodes = len(tree)-1
  if 2*node_index > num_nodes:
    return true
  else:
    return false
    
