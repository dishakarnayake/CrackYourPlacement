class Solution(object):
    def majorityElement(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        majority_element = nums[0]
        max_count = frequency[nums[0]]
        for num, count in frequency.items():
            if count > max_count:
                majority_element = num
                max_count = count
        
        return majority_element

obj = Solution()
print(obj.majorityElement([2,2,1,1,1,2,2]))