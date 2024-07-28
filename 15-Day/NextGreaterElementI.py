class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        hashMap = {n: i for i, n in enumerate(nums1)}
        
        
        res = [-1] * len(nums1)
        
        
        stack = []
        
        for num in nums2:
            
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                if smaller_num in hashMap:
                    res[hashMap[smaller_num]] = num
            
            stack.append(num)
        
        return res