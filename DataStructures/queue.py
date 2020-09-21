import os, sys

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.tail = None


  def isEmpty(self):
    return self.head == None


  def peekFront(self):
    if self.isEmpty():
      return "Queue is empty."

    return self.head.data


  def enqueue(self, data):
    new_node = Node(data)

    if self.tail != None:
      self.tail.next = new_node

    self.tail = new_node

    # if queue is empty
    if self.isEmpty():
      self.head = new_node


  def dequeue(self):
    if self.isEmpty():
      self.tail = None
      return "Queue is empty."

    dequeue_data = self.head.data
    self.head = self.head.next

    return dequeue_data


if __name__ == "__main__":
  q = Queue()
  print(q.isEmpty())

  q.enqueue(2)
  q.enqueue(8)
  print(q.peekFront())
  q.enqueue(5)
  q.dequeue()
  print(q.peekFront())
  q.dequeue()
  q.dequeue()
  q.enqueue(1)
  print(q.peekFront())
  q.dequeue()
  print(q.peekFront())
