from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of the given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Initialize a list to keep track of visited nodes.
        visited = [False] * V
        # List to store the BFS traversal result.
        bfs_result = []
        # Queue to facilitate the BFS traversal.
        q = Queue()
        
        # Start BFS from the 0th vertex.
        q.put(0)
        visited[0] = True
        
        while not q.empty():
            # Dequeue a vertex from the queue.
            node = q.get()
            bfs_result.append(node)
            
            # Iterate through the adjacent vertices of the dequeued vertex.
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    # If the neighbor hasn't been visited, enqueue it.
                    q.put(neighbor)
                    visited[neighbor] = True
        
        return bfs_result