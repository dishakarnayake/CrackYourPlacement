class Solution(object):
    def uniquePathsIII(self, grid):
        global steps
        obs = 0
        start = (0,0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    obs += 1
                if grid[i][j] == 1:
                    start = (i,j)
        steps = len(grid) * len(grid[0]) - obs

        def dfs(path, current, grid, inside):
            value = 0
            path = path + [current] 
            if grid[current[0]][current[1]] == 2 and len(path) == steps:
                return 1
            up = (current[0] - 1, current[1])
            right = (current[0], current[1] + 1)
            down = (current[0] + 1, current[1])
            left = (current[0], current[1] - 1)
            if current[0] - 1 != -1 and (up not in path and grid[current[0] - 1][current[1]] != -1):
                value += dfs(path, up, grid, inside +1)
            if current[1] + 1 != len(grid[0]) and right not in path and grid[current[0]][current[1] + 1] != -1:
                value += dfs(path, right, grid,inside +1)
            if current[0] + 1 != len(grid) and down not in path and grid[current[0] + 1][current[1]] != -1:
                value += dfs(path, down, grid,inside +1)
            if current[1] - 1 != -1 and left not in path and grid[current[0]][current[1] - 1] != -1:
                value += dfs(path, left, grid,inside +1)
            return value
        
        return dfs([],start,grid,1)
        