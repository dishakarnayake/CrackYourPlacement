from collections import deque

class Solution:
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Initialize the queue for BFS and a variable to keep track of fresh oranges
        queue = deque()
        fresh_oranges = 0
        
        # Populate the queue with initial rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform BFS
        time_elapsed = 0
        while queue:
            r, c, time = queue.popleft()
            time_elapsed = time
            
            # Explore the four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check if the new position is within bounds and has a fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Rot the fresh orange
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    # Add the new rotten orange to the queue with incremented time
                    queue.append((nr, nc, time + 1))
        
        # If there are still fresh oranges left, return -1
        if fresh_oranges > 0:
            return -1
        else:
            return time_elapsed

# Example usage:
solution = Solution()
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(solution.orangesRotting(grid))  # Output: 4
