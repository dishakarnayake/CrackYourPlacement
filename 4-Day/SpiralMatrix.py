class Solution:
    def spiralOrder(self, matrix ):
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1
        result = []
        while rows > 0 and cols > 0:
            for _ in range(cols):
                col += direction
                # print(matrix[row][col])
                result.append(matrix[row][col])
                
            rows -= 1

            for _ in range(rows):
                row += direction
                result.append(matrix[row][col])
            cols -= 1
            direction *= -1

        return result
    
obj = Solution()
print(obj.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))