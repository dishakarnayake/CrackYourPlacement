#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
        n = len(matrix)
        
        # Replace all -1 with infinity, except for the diagonal
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1 and i != j:
                    matrix[i][j] = float('inf')
        
        # Apply Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update the shortest distance between i and j by considering vertex k
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        # Replace all infinities back with -1 to indicate no path
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1