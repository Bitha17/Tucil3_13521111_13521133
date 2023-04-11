import graph as g
import astar as a

def read_file(filename):
    with open(filename) as f:
        node_names = f.readline().strip().split()
        n = len(node_names)

        coordinates = [tuple(map(float, coord[1:-1].split(','))) for coord in f.readline().strip().split()]

        graph = g.Graph(n)
        for i in range(n):
            node = g.Node(i, node_names[i], coordinates[i][0], coordinates[i][1])
            graph.addNode(node)

        adjacency_matrix = []
        for line in f:
            adjacency_matrix.append(list(map(int, line.strip().split())))

        # create a NetworkX graph from the adjacency matrix
        for i in range(n):
            for j in range(i,n):
                if adjacency_matrix[i][j] == 1:
                    edge = g.Edge(graph.nodes[i], graph.nodes[j])
                    graph.addEdge(edge)
        
        return graph, adjacency_matrix, coordinates



