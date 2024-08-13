class Solution:
    	def maxDistance(self, grid):

            rows = len(grid)
            cols = len(grid[0])
            queue = []

            for row in range(len(grid)):
                for col in range(len(grid[0])):

                    if grid[row][col] == 1:
                        queue.append((row,col,0))

            if len(queue) == rows * cols or len(queue) == 0:
                return -1

            direction = [[0,1],[1,0],[-1,0],[0,-1]]
            result = 1

            while queue:
                current_x, current_y, current_distance = queue.pop(0)

                for next_direction in direction:
                    next_x , next_y = current_x + next_direction[0] , current_y + next_direction[1]

                    if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == 0:
                        queue.append((next_x , next_y, current_distance + 1))
                        grid[next_x][next_y] = current_distance + 1
                        result = max(result, current_distance + 1)

            return result