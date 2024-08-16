from collections import deque
class Solution:
    def is_inside_board(self, x, y, N):
        return 1 <= x <= N and 1 <= y <= N

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code her
		# Possible movements for a Knight
        moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        
        # Convert 1-based index to 0-based index for easier processing
        start_x, start_y = KnightPos
        target_x, target_y = TargetPos
        
        # Queue to store the positions along with the current distance from start
        queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
        
        # Visited array to keep track of visited positions
        visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
        
        # Mark the start position as visited
        visited[start_x][start_y] = True
        
        # BFS to find the shortest path
        while queue:
            x, y, dist = queue.popleft()
            
            # If the target is reached, return the distance
            if x == target_x and y == target_y:
                return dist
            
            # Explore all possible moves for the Knight
            for move_x, move_y in moves:
                next_x, next_y = x + move_x, y + move_y
                
                if self.is_inside_board(next_x, next_y, N) and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))
        
        return -1  # In case the target is unreachablee
