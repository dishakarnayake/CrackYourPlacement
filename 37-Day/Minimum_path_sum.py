class Solution(object):
    def minPathSum(self, grid):
        i=0
        j=0
        n = len(grid)
        m = len(grid[0])
        
        costmatrix = [[0]*m for i in range(n)]

        costmatrix[0][0] = grid[0][0]
        for i in range(1,m):
            costmatrix[0][i] = costmatrix[0][i-1] + grid[0][i]
        for i in range(1,n):
            costmatrix[i][0] = costmatrix[i-1][0] + grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                costmatrix[i][j] = min(costmatrix[i-1][j], costmatrix[i][j-1]) + grid[i][j]
        return costmatrix[n-1][m-1]
        