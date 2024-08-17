from collections import defaultdict, deque

class Solution:
    def findOrder(self, alien_dict, N, K):
        # Step 1: Create a graph
        graph = defaultdict(list)
        in_degree = {chr(i + ord('a')): 0 for i in range(K)}
        
        # Step 2: Build the graph using the given dictionary
        for i in range(N - 1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            min_length = min(len(word1), len(word2))
            
            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
        
        # Step 3: Perform topological sort using Kahn's algorithm (BFS)
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If topo_order doesn't contain all characters, it means there was a cycle (invalid input)
        if len(topo_order) < K:
            return ""
        
        return "".join(topo_order)