class Solution(object):
    def uniquePaths(self, m, n):
        arr = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                arr[j] += arr[j - 1]
        return arr[-1]
        