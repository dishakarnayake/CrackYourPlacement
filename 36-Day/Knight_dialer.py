class Solution(object):
    def knightDialer(self, n):
        # Build the graph
        graph = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        # Dynamic programming
        dp0 = [1] * 10
        dp1 = [0] * 10
        for i in range(2, n + 1):
            for curr in range(10):
                for next_cell in graph[curr]:
                    dp1[next_cell] = (dp1[next_cell] + dp0[curr]) % (10**9 + 7)
            dp0, dp1 = dp1, [0] * 10

        # Summarize
        result = sum(dp0) % (10**9 + 7)
        return result
        