class Solution:
    def twoSum(self, nums, target) :
        hash_map = {}                               # Create an empty hashmap

        for i, num in enumerate(nums):
            complement = target - num               # Calculate the complement of the current number
            if complement in hash_map:              # Check if the complement is already in the hashmap
                return [hash_map[complement], i]    # Return indices of the two numbers
            hash_map[num] = i                       # Add the current number to the hashmap
        return []                                   # Return an empty list if no solution is found
    
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))