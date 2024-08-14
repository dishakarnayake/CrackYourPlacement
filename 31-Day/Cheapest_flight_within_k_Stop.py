import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = [[] for _ in range(n)]

        for flight in flights:
            u, v, w = flight
            graph[u].append((v, w))

        return self.dijkstra(graph, src, dst, k)

    def dijkstra(self, graph, src, dst, k):
        INF = float('inf')
        dist = [[INF] * (k + 2) for _ in range(len(graph))]
        minHeap = [(0, src, k + 1)]

        dist[src][k + 1] = 0

        while minHeap:
            d, u, stops = heapq.heappop(minHeap)
            if u == dst:
                return d
            if stops == 0:
                continue
            for v, w in graph[u]:
                if d + w < dist[v][stops - 1]:
                    dist[v][stops - 1] = d + w
                    heapq.heappush(minHeap, (dist[v][stops - 1], v, stops - 1))

        return -1
