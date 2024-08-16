from typing import List

class Solution:
    # Function to perform DFS and fill the stack according to finishing times
    def dfs_fill_order(self, v: int, visited: List[bool], stack: List[int], adj: List[List[int]]):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                self.dfs_fill_order(neighbor, visited, stack, adj)
        stack.append(v)

    # Function to perform DFS on the transposed graph
    def dfs(self, v: int, visited: List[bool], adj: List[List[int]]):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, adj)

    # Function to get the transpose of the graph
    def get_transpose(self, V: int, adj: List[List[int]]) -> List[List[int]]:
        transpose = [[] for _ in range(V)]
        for i in range(V):
            for neighbor in adj[i]:
                transpose[neighbor].append(i)
        return transpose

    # Function to find the number of strongly connected components using Kosaraju's algorithm
    def kosaraju(self, V: int, adj: List[List[int]]) -> int:
        stack = []
        visited = [False] * V
        
        # Step 1: Fill the stack according to finishing times
        for i in range(V):
            if not visited[i]:
                self.dfs_fill_order(i, visited, stack, adj)
        
        # Step 2: Get the transposed graph
        transpose = self.get_transpose(V, adj)
        
        # Step 3: Do DFS according to the finishing times in the reversed graph
        visited = [False] * V
        count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                self.dfs(v, visited, transpose)
                count += 1
        
        return count