class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []
        self.g = -1
        self.h = -1
        self.f = -1
        self.parent = None
    
    def addNeighbor(self,neighbor):
        self.neighbors.append(neighbor)

class Edge:
    def __init__(self,source,target):
        self.source = source
        self.target = target

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self,node):
        self.nodes.append(node)

    def addEdge(self,edge):
        edge.source.addNeighbor(edge.target)
        edge.target.addNeighbor(edge.source)
        self.edges.append(edge)
        