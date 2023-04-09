import math

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = []
        self.g = math.inf
        self.h = math.inf
        self.f = math.inf
        self.parent = None
    
    def addNeighbor(self,neighbor):
        self.neighbors.append(neighbor)

    def __lt__(self,other):
        return self.f < other.f

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
        