def isSafe(node, graph, color, c, V):
    # Check if any adjacent vertex has the same color
    for i in range(V):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True

def graphColoringUtil(graph, m, color, node, V):
    # If all vertices are assigned a color, return True
    if node == V:
        return True
    
    # Try different colors for vertex node
    for c in range(1, m+1):
        if isSafe(node, graph, color, c, V):
            color[node] = c
            # Recur to assign colors to the rest of the vertices
            if graphColoringUtil(graph, m, color, node + 1, V):
                return True
            # If assigning color c doesn't lead to a solution, backtrack
            color[node] = 0
    
    return False

def graphColoring(graph, m, V):
    # Initialize all vertices with no color (0)
    color = [0] * V
    
    # Start coloring from the first vertex (node 0)
    if graphColoringUtil(graph, m, color, 0, V):
        return 1
    return 0