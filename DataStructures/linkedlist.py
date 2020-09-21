import os, sys

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def printLinkedList(self):
    if self.head == None:
      print("Linked list is empty.")
      return

    current_node = self.head
    while current_node != None:
      print(current_node.data, ", ", sep = '', end = '')
      current_node = current_node.next

    print()


  def insertAtIndex(self, data, index):
    # create new node to be inserted
    new_node = Node(data)

    # if linked list is empty or should insert at beginning
    if self.head == None or index == 0:
      new_node.next = self.head
      self.head = new_node
      return

    # else
    current_node = self.head
    i = 0
    while i < index:
      current_node = current_node.next
      i += 1

    new_node.next = current_node.next
    current_node.next = new_node


  def insertAtNode(self, data, prev_node):
    # create new node to be inserted
    new_node = Node(data)

    new_node.next = prev_node.next
    prev_node.next = new_node


  def deleteWithValue(self, data_to_delete):
    # if linked list is empty
    if self.head == None:
      print("List is empty. Cannot delete.")
      return

    # if we need to delete head
    if self.head.data == data_to_delete:
      self.head = self.head.next
      return

    # else
    current_node = self.head
    while current_node.next != None:
      if current_node.next.data == data_to_delete:
        current_node.next = current_node.next.next
        break
      current_node = current_node.next


if __name__ == "__main__":
  ll = LinkedList()
  ll.printLinkedList()

  ll.insertAtIndex(2, 0)
  ll.insertAtIndex(4, 0)
  ll.insertAtIndex(6, 1)
  ll.insertAtIndex(8, 1)
  ll.insertAtIndex(10, 3)
  ll.printLinkedList()

  ll.deleteWithValue(4)
  ll.deleteWithValue(6)
  ll.printLinkedList()
