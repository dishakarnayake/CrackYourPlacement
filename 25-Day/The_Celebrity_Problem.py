class Solution:
    def celebrity(self, mat):
        n = len(mat)
        a = 0
        b = n - 1

        # Step 1: Find a potential celebrity
        while a < b:
            if mat[a][b] == 1:
                a += 1  # a knows b, so a cannot be a celebrity
            else:
                b -= 1  # a does not know b, so b cannot be a celebrity

        # Step 2: Verify if the candidate is a celebrity
        candidate = a

        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate