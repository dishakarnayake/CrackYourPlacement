import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # Initialize a priority queue to pick the minimum weight edge at each step.
        pq = []
        # To keep track of vertices included in MST.
        in_mst = [False] * V
        # Start with the first vertex (you can start with any vertex).
        heapq.heappush(pq, (0, 0))  # (weight, vertex)
        total_weight = 0

        while pq:
            weight, u = heapq.heappop(pq)

            # If the vertex u is already in the MST, skip it.
            if in_mst[u]:
                continue
            
            # Include the vertex in the MST.
            in_mst[u] = True
            total_weight += weight

            # Explore the neighbors of u.
            for v, w in adj[u]:
                if not in_mst[v]:
                    heapq.heappush(pq, (w, v))

        return total_weight