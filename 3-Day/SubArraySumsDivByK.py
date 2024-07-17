class Solution(object):
    def subarraysDivByK(self, nums, k):
        res = 0
        prefix = [] 
        prefix_mod = [0]
        for x in nums:          
            if len(prefix) != 0:
                prefix.append(prefix[-1] + x)
            else:
                prefix.append(x)
            
            prefix_mod.append(prefix[-1] % k)
            
        print(prefix_mod)
        d = {}
        for x in prefix_mod:
            if x in d:
                res += d[x]
                d[x] += 1
            else:
                d[x] = 1        
        
        return res
    
obj = Solution()
print(obj.subarraysDivByK([4,5,0,-2,-3,1],5))