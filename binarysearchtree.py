import os, sys

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinarySearchTree:
  def __init__(self):
    self.root = None


  def inorderTraversal(self, current_node):
    if current_node == None:
      return

    self.inorderTraversal(current_node.left)
    print(current_node.data, ", ", sep='', end='')
    self.inorderTraversal(current_node.right)


  def preorderTraversal(self, current_node):
    if current_node == None:
      return

    print(current_node.data, ", ", sep='', end='')
    self.inorderTraversal(current_node.left)
    self.inorderTraversal(current_node.right)


  def postorderTraversal(self, current_node):
    if current_node == None:
      return

    self.inorderTraversal(current_node.left)
    self.inorderTraversal(current_node.right)
    print(current_node.data, ", ", sep='', end='')

  # calculte height of BST
  def heightBST(self, node):
      if node == None or (node.right == None and node.left == None):
        return 0
      return max(self.heightBST(node.right), self.heightBST(node.left)) + 1


  def insertIntoBST(self, data):
    new_node = Node(data)

    # if tree is empty
    if self.root == None:
      self.root = new_node
      return

    current_node = self.root
    while current_node != None:
      # insert into left subtree
      if data < current_node.data:
        if current_node.left == None:
          current_node.left = new_node
          break
        current_node = current_node.left
      else:
        # insert int0 right subtree
        if current_node.right == None:
          current_node.right = new_node
          break
        current_node = current_node.right


  def findInBST(self, data):
    # if tree is empty
    if self.root == None:
      print("Tree is empty")
      return

    current_node = self.root
    while current_node != None:
      if data == current_node.data:
        print("Found in tree:", data)
        return True
      elif data < current_node.data:
        # search in left subtree
        current_node = current_node.left
      else:
        # search in right subtree
        current_node = current_node.right

    print("Could not find in tree:", data)
    return False


  def findReplacement(self, node):
    # find inorder successor of node - i.e. leftmost leaf
    current_node = node

    while current_node.left != None:
      current_node = current_node.left

    return current_node


  def deleteFromBST(self, current_node, data):
    if current_node == None:
      return current_node

    if data < current_node.data:
      current_node.left = self.deleteFromBST(current_node.left, data)
    elif data > current_node.data:
      current_node.right = self.deleteFromBST(current_node.right, data)
    else:
      # node is leaf or has one child
      if current_node.left == None:
        temp = current_node.right
        current_node = None
        return temp
      elif current_node.right == None:
        temp = current_node.left
        current_node = None
        return temp

      # node has 2 children
      replacement = self.findReplacement(current_node.right)
      # copy node with replacement's contents
      current_node.data = replacement.data
      # delete replacement from BST
      current_node.right = self.deleteFromBST(current_node.right, replacement.data)

    return current_node


if __name__ == "__main__":
  bst = BinarySearchTree()
  bst.insertIntoBST(5)
  bst.insertIntoBST(10)
  bst.insertIntoBST(3)
  bst.insertIntoBST(4)
  bst.insertIntoBST(2)
  bst.insertIntoBST(8)
  bst.insertIntoBST(12)
  bst.insertIntoBST(7)
  bst.insertIntoBST(9)
  bst.inorderTraversal(bst.root)
  print()
  bst.findInBST(8)
  bst.findInBST(1)
  bst.deleteFromBST(bst.root, 2)
  bst.inorderTraversal(bst.root)
  print()
  bst.deleteFromBST(bst.root, 8)
  bst.inorderTraversal(bst.root)
  print()
  print(bst.heightBST(bst.root))