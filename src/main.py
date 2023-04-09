import astar
import readfile as r

graph = r.read_file("../test/test.txt")
start_name = input("Start point: ")
end_name = input("End point: ")

for node in graph.nodes:
    if node.name == start_name:
        start = node
    if node.name == end_name:
        end = node

path, dist = astar.astar(graph, start, end)

if path != None:
    for node in path:
        print(node.name, end=" ")
    print()
    print(dist)
else:
    print("no path")