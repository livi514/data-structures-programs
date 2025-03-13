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
      #so for each node, we would have to check whether the node has a left child and a right child
      left_child = find_left_child(node)
      right_child = find_right_child(node)
      if left_child == -1:
        is_left_child == false
      else:
        is_left_child == true
      if right_child == -1:
        is_right_child == false
      else: 
        is_right_child == true
      node_index = tree.index(node)
      if is_left_child == true and is_right_child == true:
        #this means that the new node cannot be a child of this node
        pass
      elif is_left_child == false:
        left_child_index = node_index*2
        tree[left_child_index] = node
      else:
        right_child_index == node_index*2+1
        tree[right_child_index] = node

def find_left_child(node):
  node_index = tree.index(node)
  num_nodes = len(tree)-1
  if 2*node_index <= num_nodes:
    left_child_index = node_index*2
    return tree[left_child_index]
  else:
    return -1 #indicates that the node has no left child

def find_right_child(node):
  node_index = tree.index(node)
  num_nodes = len(tree)-1
  if 2*node_index + 1 <= num_nodes:
    right_child_index = node_index*2+1
    return tree[right_child_index]
  else:
    return -1 #indicates that the node has no right child

def find_parent(node):
  node_index = tree.index(node)
  if node_index > 1:
    parent_index = node_index//2
    return tree[parent_index]
  else:
    return -1 #indicates that the node has no parents

def find_root(node):
  if len(tree) > 0:
    return tree[1]
  else:
    return -1 #indicates tree is empty

def is_node_leaf(node):
  node_index = tree.index(node)
  num_nodes = len(tree)-1
  if 2*node_index > num_nodes:
    return true
  else:
    return false
    
