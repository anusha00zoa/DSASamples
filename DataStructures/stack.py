import os, sys

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None


  def isEmpty(self):
    return self.top == None


  def peekAtTop(self):
    if self.isEmpty():
      print("Stack is empty.")
      return

    print(self.top.data)


  def push(self, data):
    new_node = Node(data)

    # if stack is empty
    if self.isEmpty():
      self.top = new_node
      return

    new_node.next = self.top
    self.top = new_node


  def pop(self):
    if self.isEmpty():
      print("Stack is empty.")
      return

    pop_data = self.top.data
    self.top = self.top.next
    return pop_data



if __name__ == "__main__":
  s = Stack()
  s.isEmpty()

  s.push(4)
  s.push(5)
  s.peekAtTop()
  s.push(8)
  s.pop()
  s.peekAtTop()
  s.pop()
  s.peekAtTop()
