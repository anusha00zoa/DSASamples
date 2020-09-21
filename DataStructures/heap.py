import os, sys

class Node:
  def __init__(self, data):
    self.data = data
    # self.left = None
    # self.right = None
    # self.parent = None


class Heap:
  def __init__(self):
    self.heap = []


  # check if heap is empty
  def isEmpty(self):
    return len(self.heap) == 0


  def getLeftChild(self, index):
    return (2 * index) + 1


  def getRightChild(self, index):
    return (2 * index) + 2


  # print root of our heap
  def peekAtTop(self):
    if not self.isEmpty():
      print(self.heap[0])


  def swap(self, i, j):
    temp = self.heap[i]
    self.heap[i] = self.heap[j]
    self.heap[j] = temp


  # build a min heap
  def minHeapify(self, l, index):
    smallest = index
    left = self.getLeftChild(index)
    right = self.getRightChild(index)

    # see if left child is smaller than current value
    if left < l and self.heap[index] > self.heap[left]:
      smallest = left

    # see if right child is smaller than current value
    if right < l and self.heap[smallest] > self.heap[right]:
      smallest = right

    # swap if needed
    if smallest != index:
      self.swap(index, smallest)
      self.minHeapify(l, smallest)


  def maxHeapify(self, l, index):
    largest = index
    left = self.getLeftChild(index)
    right = self.getRightChild(index)

    # see if left child is larger than current value
    if left < l and self.heap[index] < self.heap[left]:
      largest = left

    # see if right child is larger than current value
    if right < l and self.heap[largest] < self.heap[right]:
      largest = right

    # swap if needed
    if largest != index:
      self.swap(index, largest)
      self.maxHeapify(l, largest)


  def insertIntoHeap(self, data, isMinHeap = True):
    # append to the end of the array representing our heap
    self.heap.append(data)

    l = len(self.heap)
    if isMinHeap:
      for i in range(l//2 - 1, -1, -1):
        self.minHeapify(l, i)
    else:
      for i in range(l//2 - 1, -1, -1):
        self.maxHeapify(l, i)



if __name__ == "__main__":
  h = Heap()
  # h.insertIntoHeap(10, False)
  # h.insertIntoHeap(15, False)
  # h.insertIntoHeap(30, False)
  # h.insertIntoHeap(40, False)
  # h.insertIntoHeap(50, False)
  # h.insertIntoHeap(100, False)
  # print(h.heap)
  h.insertIntoHeap(100)
  h.insertIntoHeap(15)
  h.insertIntoHeap(50)
  h.insertIntoHeap(40)
  h.insertIntoHeap(30)
  h.insertIntoHeap(10)
  print(h.heap)
