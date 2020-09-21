# Python program for Kruskal's algorithm to find Minimum Spanning Tree of a given connected,
# undirected and weighted graph
from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = []


  # function to add an edge to graph
  def addEdge(self, u, v, w):
    self.graph.append([u, v, w])


  # A utility function to find set of an element i
  def find(self, parent, i):
    if parent[i] == i:
      return i
    return self.find(parent, parent[i])


  # A function that does union of two sets of x and y
  def union(self, parent, rank, x, y):
    xroot = self.find(parent, x)
    yroot = self.find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    if rank[xroot] < rank[yroot]:
      parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
      parent[yroot] = xroot
    else:
      # If ranks are same, then make one as root and increment its rank by one
      parent[yroot] = xroot
      rank[xroot] += 1


  # The main function to construct MST
  def KruskalMST(self):
    result = []
    i = 0
    e = 0 # edge counter
    parent = []
    rank = []

    # Sort all edges in non-decreasing order of their weight.
    self.graph = sorted(self.graph, key=lambda item: item[2])

    for node in range(self.V):
      parent.append(node)
      rank.append(0)

    while e < self.V - 1:
      # Pick the smallest edge and increment the index for next iteration
      u, v, w = self.graph[i]
      i = i + 1
      x = self.find(parent, u)
      y = self.find(parent, v)

      # print("u =", u, ", parent[u] =", x, ", v =", v, ", parent[v] =", y)
      # If including this edge does't cause cycle, include it in result
      if x != y:
        e = e + 1
        result.append([u, v, w])
        self.union(parent, rank, x, y)

      # print("parent =", parent)
      # print("rank =", rank)

    # print the built MST
    print ("The constructed MST:")
    for u, v, weight in result:
      print("%d - %d == %d" % (u, v, weight))


if __name__ == "__main__":
  g = Graph(4)
  g.addEdge(0, 1, 10)
  g.addEdge(0, 2, 6)
  g.addEdge(0, 3, 5)
  g.addEdge(1, 3, 15)
  g.addEdge(2, 3, 4)

  g.KruskalMST()
