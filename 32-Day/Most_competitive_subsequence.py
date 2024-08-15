class Solution(object):
    def mostCompetitive(self, nums, k):
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(nums) - i > k - len(stack):
                stack.pop()
            stack.append(n)
        return stack[:k]
        