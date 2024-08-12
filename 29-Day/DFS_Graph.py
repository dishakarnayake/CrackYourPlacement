#User function Template for python3

class Solution:
    def dfs(self, node, adj, visited, dfs_result):
        # Mark the current node as visited and add it to the result list.
        visited[node] = True
        dfs_result.append(node)
        
        # Traverse all the vertices adjacent to the current node.
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited, dfs_result)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        # Initialize a list to keep track of visited nodes.
        visited = [False] * V
        # List to store the DFS traversal result.
        dfs_result = []
        
        # Start DFS from the 0th vertex.
        self.dfs(0, adj, visited, dfs_result)
        
        return dfs_result