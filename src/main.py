import astar
import readfile as r
import matplotlib.pyplot as plt
import visualize as v

graph, adj, coor = r.read_file("../test/test.txt")
# v.visualize1(graph, adj, coor)

start_name = input("Start point: ")
end_name = input("End point: ")


for node in graph.nodes:
    if node.name == start_name:
        start = node
    if node.name == end_name:
        end = node

path, dist = astar.astar(start, end)


if path != None:
    for node in path:
        print(node.name, end=" ")
    print()
    print(dist)
else:
    print("no path")

# v.visualize2(graph, path, adj, coor)