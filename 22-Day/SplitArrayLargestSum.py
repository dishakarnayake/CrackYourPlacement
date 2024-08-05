class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # Edge case: When there's no splits required at all
        if k == 1:
            return sum(nums)

        # logic 
        left, right = max(nums), sum(nums)
        while left <= right :
            mid = ( left + right ) // 2
            summ = 0
            splits = 1
            for i in nums:
                summ += i
                if summ <= mid:
                    continue
                else:
                    splits += 1
                    summ = i
            
            # no. of splits exceeds the required splits
            if splits > k:
                left = mid + 1
            
            # if no. of splits are equal or lower than required splits
            # This case is also applicable in 'splits == k', because ???? (refer the pinned comment)
            else:
                right = mid - 1
        
        return left