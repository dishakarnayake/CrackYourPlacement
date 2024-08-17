class Solution:
    
    #Function to return list containing vertices in Topological order.
   
        # Code here
        # Helper function for DFS
    def dfs(self, v, visited, stack, adj):
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all the vertices adjacent to this vertex
        for i in adj[v]:
            if not visited[i]:
                self.dfs(i, visited, stack, adj)
        
        # Push the current vertex to the stack which stores the result
        stack.append(v)
    
    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Initialize all vertices as not visited
        visited = [False] * V
        stack = []
        
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(V):
            if not visited[i]:
                self.dfs(i, visited, stack, adj)
        
        # Return the contents of the stack in reverse order
        # since the vertices were added to the stack in postorder
        return stack[::-1]