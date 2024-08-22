class Solution(object):
    def trap(self, height):
        n = len(height) # Number of elements in the input array
        water = 0       # Variable to store the total trapped water

        # Arrays to store maximum height to the left and right of each index
        l_max = [0] * n
        r_max = [0] * n

        # Calculate the maximum height to the left of each index
        l_max[0] = height[0] # First element's maximum height to the left is itself
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])

        # Calculate the maximum height to the right of each index
        r_max[n - 1] = height[n - 1] # Last element's maximum height to the right is itself
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])

        # Iterate through each index (excluding the first and last)
        for i in range(1, n - 1):
            # Calculate the maximum water current height can hold above itself
            water += min(r_max[i], l_max[i]) - height[i]

        return water # Return the total trapped water
        