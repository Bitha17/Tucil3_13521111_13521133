import graph as g

def read_file(filename):
    with open(filename) as f:
        node_names = f.readline().strip().split()

        coordinates = [tuple(map(int, coord[1:-1].split(','))) for coord in f.readline().strip().split()]

        graph = g.Graph()
        for i in range(len(node_names)):
            node = g.Node(node_names[i], coordinates[i][0], coordinates[i][1])
            graph.addNode(node)

        adjacency_matrix = []
        for line in f:
            adjacency_matrix.append(list(map(int, line.strip().split())))

        for i in range(len(node_names)):
            for j in range(i,len(node_names)):
                if adjacency_matrix[i][j] == 1:
                    edge = g.Edge(graph.nodes[i], graph.nodes[j])
                    graph.addEdge(edge)

        # for node in graph.nodes:
        #     print(node.name, node.x, node.y)
        #     for neighbor in node.neighbors:
        #         print(neighbor.name, end=" ")
        #     print()

        return graph