import networkx as nx
import matplotlib.pyplot as plt
import graph as g
import astar as a

def read_file(filename):
    with open(filename) as f:
        node_names = f.readline().strip().split()
        n = len(node_names)

        coordinates = [tuple(map(int, coord[1:-1].split(','))) for coord in f.readline().strip().split()]

        graph = g.Graph()
        for i in range(n):
            node = g.Node(node_names[i], coordinates[i][0], coordinates[i][1])
            graph.addNode(node)

        adjacency_matrix = []
        for line in f:
            adjacency_matrix.append(list(map(int, line.strip().split())))

        # create a NetworkX graph from the adjacency matrix
        G = nx.DiGraph()
        edge_labels = {}
        for i in range(n):
            for j in range(i,n):
                if adjacency_matrix[i][j] == 1:
                    edge = g.Edge(graph.nodes[i], graph.nodes[j])
                    graph.addEdge(edge)
                    G.add_edge(i,j)
                    edge_labels[(i,j)] = a.eucilidean(graph.nodes[i],graph.nodes[j])

        # set the node labels to be the node names
        labels = {}
        for i, node_name in enumerate(node_names):
            labels[i] = node_name
        
        # draw the graph with labels
        nx.draw(G, coordinates, with_labels=True, labels=labels, arrows=False)
        nx.draw_networkx_edge_labels(G, coordinates, edge_labels=edge_labels)
        
        return graph



