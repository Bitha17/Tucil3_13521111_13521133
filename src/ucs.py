import math
import heapq
import graph
import astar

def ucs(start, end):

    # Searching queue
    heap = []
    heapq.heappush(heap, start)

    # Iterating answer
    while heap :
        current = heapq.heappop(heap)
        current.checked = True

        # Check if current is the goal
        if current == end :
            path = []
            dist = 0
            while current:
                path.append(current)
                if current.parent != None :
                    dist += astar.eucilidean(current, current.parent)
                current = current.parent
            
            # Returning expected UCS path
            return path[::-1], dist
        
        # Checking any available node
        status = False
        for node in current.neighbors :
            if node.checked == False :
                status = True

        # Checking closest node
        if status :
            tobechecked = []
            for node in current.neighbors :
                if node.checked == False :
                    heapq.heappush(tobechecked, node)
            compdist = []
            for node in tobechecked :
                heapq.heappush(compdist, astar.eucilidean(current, node))
            i = 0
            idx = 0
            mindist = compdist[0]
            for dist in compdist :
                i += 1
                if dist < mindist :
                        mindist = dist
                        idx = i
            tobechecked[idx].parent = current
        
            # Push to current path
            heapq.heappush(heap, tobechecked[idx])
               
        else :
            break

    return None, math.inf