import networkx as nx
import astar as a
import matplotlib.pyplot as plt
import numpy as np

def visualize1(graph,adj,coordinates,ax):
    G = nx.Graph()
    edge_labels = {}
    for i in range(graph.n):
            for j in range(i,graph.n):
                if adj[i][j] == 1:
                    G.add_edge(i,j)
                    edge_labels[(i,j)] = round(a.eucilidean(graph.nodes[i],graph.nodes[j]),4)
            if not graph.nodes[i].neighbors:
                G.add_node(i)
    # set the node labels to be the node names
    labels = {}
    for i in range(graph.n):
        labels[i] = graph.nodes[i].name
    
    # draw the graph with labels
    nx.draw_networkx(G, coordinates, with_labels=True, labels=labels, arrows=False,ax=ax)
    nx.draw_networkx_edge_labels(G, coordinates, edge_labels=edge_labels,ax=ax)

    # plt.show()

def visualize2(graph,path,adj,coordinates,ax):
    G = nx.Graph()
    edge_labels = {}
    edge_colors = {}
    if path is not None:
        for i in range(len(path)-1):
            edge_colors[(path[i].id, path[i+1].id)] = 'red'

    for i in range(graph.n):
            for j in range(i,graph.n):
                if adj[i][j] == 1:
                    G.add_edge(i,j)
                    edge_labels[(i,j)] = round(a.eucilidean(graph.nodes[i],graph.nodes[j]),4)
                    if (i,j) not in edge_colors and (j,i) not in edge_colors:
                        edge_colors[(i,j)] = 'black'
            if not graph.nodes[i].neighbors:
                G.add_node(i)
    sort = dict(sorted(edge_colors.items()))
    colors = np.array(list(sort.values()))

    # set the node labels to be the node names
    labels = {}
    for i in range(graph.n):
        labels[i] = graph.nodes[i].name
    
    # draw the graph with labels
    nx.draw_networkx(G, coordinates, with_labels=True, labels=labels, arrows=False,ax=ax)
    nx.draw_networkx_edges(G, coordinates, edge_color=colors,ax=ax)
    nx.draw_networkx_edge_labels(G, coordinates, edge_labels=edge_labels,ax=ax)

    # plt.show()