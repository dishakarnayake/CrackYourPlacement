class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = defaultdict(int)
        dp[(0,0)] = 0
        ans = 0

        for s in strs:
            zero,one = s.count('0'),s.count('1')
            nextDp = dp.copy()
            for key,val in dp.items():
                countZero,countOne = zero+key[0],one+key[1]
                if countZero<=m and countOne<=n:
                    nextDp[(countZero,countOne)] = max(nextDp[(countZero,countOne)],1+val)
                    ans = max(ans,nextDp[(countZero,countOne)])
            dp = nextDp

        return ans
        