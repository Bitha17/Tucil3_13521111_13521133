import math
import heapq
import astar

def ucs(start, end):

    # Searching queue
    queue = []
    heapq.heappush(queue, (0,start,[start]))

    # Iterating answer
    while queue :
        (dist, current, path) = heapq.heappop(queue)

        if current.checked:
            continue

        current.checked = True

        # Check if current is the goal
        if current == end :            
            # Returning expected UCS path
            return path, dist
        
        for neighbor in current.neighbors:
            if neighbor.checked:
                continue
            new_dist = dist + astar.eucilidean(neighbor, current)
            heapq.heappush(queue, (new_dist,neighbor,path+[neighbor]))

    return None, math.inf