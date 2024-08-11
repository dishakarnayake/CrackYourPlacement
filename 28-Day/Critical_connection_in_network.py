class Solution:
    
    def dfs_util(self, parent, vertex, adj_list, visited, min_visited, level, critical_edge):   
        visited[vertex] = level
        min_visited[vertex] = level

        children = adj_list[vertex]

        for child in children:
            if child == parent:
                continue
            if child not in visited:
                self.dfs_util(vertex, child, adj_list, visited, min_visited, level+1, critical_edge)
            min_level_visited = min_visited[child]
            if min_level_visited > level:
                critical_edge.append([vertex, child])
            min_visited[vertex] = min(min_visited[vertex], min_visited[child])            

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = self.convert_to_adj_list(connections)
        critical_edges = []
        self.dfs_util(-1, 0, adj_list, {}, {}, 0, critical_edges)
        return critical_edges
    def convert_to_adj_list(self, connections):
        adj_list = {}
        for con in connections:
            if con[0] not in adj_list:
                adj_list[con[0]] = set()
            if con[1] not in adj_list:
                adj_list[con[1]] = set()
            adj_list[con[0]].add(con[1])
            adj_list[con[1]].add(con[0])
        return adj_list