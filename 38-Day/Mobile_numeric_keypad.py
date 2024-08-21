class Solution:
	def getCount(self, n):
		# code here
		if n == 1:
            return 10  # If n = 1, all digits (0-9) are possible

        # Mapping of each digit to the digits it can move to
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # Initialize the dp array where dp[i][j] represents the number of sequences
        # of length i that end with digit j
        dp = [[0] * 10 for _ in range(n + 1)]

        # Base case: There is 1 sequence of length 1 for each digit
        for i in range(10):
            dp[1][i] = 1

        # Fill the dp array for lengths 2 to n
        for length in range(2, n + 1):
            for digit in range(10):
                dp[length][digit] = sum(dp[length - 1][move] for move in moves[digit])

        # The result is the sum of all sequences of length n, starting from any digit
        return sum(dp[n][i] for i in range(10))