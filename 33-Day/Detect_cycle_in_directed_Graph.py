from typing import List

class Solution:
    
    def isCyclicUtil(self, v: int, visited: List[bool], recStack: List[bool], adj: List[List[int]]) -> bool:
        # Mark the current node as visited and add it to the recursion stack
        visited[v] = True
        recStack[v] = True
        
        # Recur for all vertices adjacent to this vertex
        for neighbor in adj[v]:
            # If the adjacent node is not visited, then recur for that node
            if not visited[neighbor]:
                if self.isCyclicUtil(neighbor, visited, recStack, adj):
                    return True
            # If the adjacent vertex is in the recursion stack, then there's a cycle
            elif recStack[neighbor]:
                return True
        
        # Remove the vertex from recursion stack
        recStack[v] = False
        return False
    
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize visited and recursion stack arrays
        visited = [False] * V
        recStack = [False] * V
        
        # Call the recursive helper function to detect cycle in different DFS trees
        for i in range(V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, recStack, adj):
                    return True
        
        return False
