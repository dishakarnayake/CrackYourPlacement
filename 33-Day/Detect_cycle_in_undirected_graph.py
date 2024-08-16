from typing import List
class Solution:
    def isCycleUtil(self, v: int, visited: List[bool], parent: int, adj: List[List[int]]) -> bool:
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all vertices adjacent to this vertex
        for neighbor in adj[v]:
            # If an adjacent vertex is not visited, recur for that vertex
            if not visited[neighbor]:
                if self.isCycleUtil(neighbor, visited, v, adj):
                    return True
            # If an adjacent vertex is visited and is not the parent of the current vertex, then there's a cycle
            elif neighbor != parent:
                return True
        
        return False
    
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Mark all the vertices as not visited
        visited = [False] * V
        
        # Call the recursive helper function to detect cycle in different DFS trees
        for i in range(V):
            if not visited[i]:  # Don't revisit already visited vertices
                if self.isCycleUtil(i, visited, -1, adj):
                    return True
        
        return False