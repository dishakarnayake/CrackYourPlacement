from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]
        
        def solve(x, y, path):
            if x == n - 1 and y == n - 1:  # Destination reached
                paths.append(path)
                return
            
            # Mark this cell as visited
            visited[x][y] = True
            
            # Move Down
            if is_safe(x + 1, y):
                solve(x + 1, y, path + 'D')
            
            # Move Left
            if is_safe(x, y - 1):
                solve(x, y - 1, path + 'L')
            
            # Move Right
            if is_safe(x, y + 1):
                solve(x, y + 1, path + 'R')
            
            # Move Up
            if is_safe(x - 1, y):
                solve(x - 1, y, path + 'U')
            
            # Backtrack: Unmark this cell as visited for other paths
            visited[x][y] = False
        
        n = len(m)
        if m[0][0] == 0:  # If the start cell is blocked
            return []
        
        paths = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        solve(0, 0, "")
        
        return sorted(paths)  # Returning sorted paths