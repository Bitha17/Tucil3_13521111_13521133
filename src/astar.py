import math
import heapq
import graph

def eucilidean(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def astar(start, end):
    # Inisialisasi nilai g, h, dan f
    start.g = 0
    start.h = eucilidean(start, end)
    start.f = start.g + start.h

    heap = []
    heapq.heappush(heap, start)

    while heap:
        current = heapq.heappop(heap)

        if current == end:
            path = []
            dist = current.f
            while current:
                path.append(current)
                current = current.parent
            return path[::-1], dist
        
        for neighbor in current.neighbors:
            temp_g = current.g + eucilidean(current,neighbor)

            if temp_g < neighbor.g:
                neighbor.g = temp_g
                neighbor.h = eucilidean(neighbor,end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current
                heapq.heappush(heap, neighbor)

    return None, math.inf