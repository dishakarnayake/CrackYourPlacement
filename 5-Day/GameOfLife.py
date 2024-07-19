class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        def count_live_neighbors(row, col):
            live_count = 0
            for dx, dy in directions:
                neighbor_row, neighbor_col = row + dx, col + dy
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    if board[neighbor_row][neighbor_col] == 1 or board[neighbor_row][neighbor_col] == 2:
                        live_count += 1
            return live_count
        for i in range(rows):
            for j in range(cols):
                # Count live neighbors
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = -1 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0  # Convert dead cell (was alive) to 0
                elif board[i][j] == -1:
                    board[i][j] = 1  # Convert live cell (was dead) to 1
                    
obj = Solution()
print(obj.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))