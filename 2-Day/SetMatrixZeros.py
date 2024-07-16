class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        print(rows)
        cols = len(matrix[0])
        print(cols)
        row_set = set()
        col_set = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
        return matrix
        
        
obj = Solution()
print(obj.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))