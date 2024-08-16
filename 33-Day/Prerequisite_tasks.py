#User function Template for python3
from collections import deque, defaultdict
class Solution:
    def isPossible(self,N,P,prerequisites):
        # Create an adjacency list for the graph
        adj = defaultdict(list)
        in_degree = [0] * N  # In-degree array to track the number of incoming edges

        # Build the graph and fill the in-degree array
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        # Initialize the queue with all nodes with in-degree 0
        queue = deque([i for i in range(N) if in_degree[i] == 0])
        count = 0  # To count the number of nodes processed

        # Process the graph
        while queue:
            node = queue.popleft()
            count += 1

            # Decrease the in-degree of all neighbors
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we processed all nodes, there was no cycle
        return count == N
    