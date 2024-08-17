from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        # Initialize a color array to store the color of each vertex
        color = [-1] * V  # -1 indicates that the vertex is uncolored
        
        # Check each component of the graph
        for i in range(V):
            # If the vertex is not colored, perform BFS from it
            if color[i] == -1:
                if not self.bfs_check(i, adj, color):
                    return False
        
        return True
    
    def bfs_check(self, start, adj, color):
        # Initialize the queue and color the start node with color 0
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            
            # Traverse all adjacent vertices of the current node
            for neighbor in adj[node]:
                # If the neighbor is not colored, color it with the opposite color
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                # If the neighbor has the same color as the current node, the graph is not bipartite
                elif color[neighbor] == color[node]:
                    return False
        
        return True