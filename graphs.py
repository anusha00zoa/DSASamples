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


class Graph:
  # a class that represents a undirected graph
  # using a dictionary to represent an adjacency list
  def __init__(self, v):
    self.vertices = v
    self.graph_main = {}


  def addEdge(self, src, dest):
    # edges are bi-directional
    if src in self.graph_main:
      self.graph_main[src].append(dest)
    else:
      self.graph_main[src] = [dest]

    if dest in self.graph_main:
      self.graph_main[dest].append(src)
    else:
      self.graph_main[dest] = [src]


  def printGraph(self):
    for vertex in self.graph_main:
      print("Vertex ", vertex, ": ", sep ='', end ='')
      print(self.graph_main[vertex])


  def printBFS(self, src):
    isVisited = [False] * len(self.graph_main)
    toBeVisitedQueue = Queue()

    isVisited[src] = True
    toBeVisitedQueue.enqueue(src)

    print("BFS traversal of graph starting at ", src, ": ", sep = '', end = '')
    while toBeVisitedQueue.isEmpty() == False:
      # dequeue first element and print it
      node = toBeVisitedQueue.dequeue()
      print(node, ", ", sep = '', end = '')

      # add children of node to queue
      for vertex in self.graph_main[node]:
        if isVisited[vertex] == False:
          toBeVisitedQueue.enqueue(vertex)
          isVisited[vertex] = True

    print()


  def DFSUtil(self, src, isVisited):
    isVisited[src]= True
    print(src, ", ", sep = '', end = '')

    for vertex in self.graph_main[src]:
      if isVisited[vertex] == False:
        self.DFSUtil(vertex, isVisited)


  def printDFS(self, src):
    isVisited = [False] * len(self.graph_main)
    print("DFS traversal of graph starting at ", src, ": ", sep='', end='')
    self.DFSUtil(src, isVisited)
    print()


if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.printGraph()
    g.printBFS(0)
    g.printDFS(0)
