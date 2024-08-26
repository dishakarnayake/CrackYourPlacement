class Solution(object):
    def solveSudoku(self, board):
        
        def isValid(board, row, col, num):
            
            for i in range(9):
                
                if board[row][i] == num or board[i][col] == num:
                    return False
                
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                    return False
            return True
        
        
        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    
                    if board[row][col] == '.':
                        for num in '123456789':
                            
                            if isValid(board, row, col, num):
                                board[row][col] = num
                                
                                if backtrack(board):
                                    return True
                                
                                board[row][col] = '.'
                        return False
            return True
        
        
        backtrack(board)