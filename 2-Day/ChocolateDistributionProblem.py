class Solution:
    def findMinDiff(self, A, N, M):
        # If there are no chocolates or students
        if M == 0 or N == 0:
            return 0
        
        # Sort the given packets
        A.sort()
        
        # Number of students cannot be more than number of packets
        if N < M:
            return -1
        
        # Initialize the minimum difference
        min_diff = float('inf')
        
        # Find the minimum difference
        for i in range(N - M + 1):
            diff = A[i + M - 1] - A[i]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff

# Example usage
sol = Solution()
A = [3, 4, 1, 9, 56, 7, 9, 12]
N = len(A)
M = 5
print(sol.findMinDiff(A, N, M))  # Output: 6
