class Solution(object):
    def maxScore(self, cardPoints, k):
        best = total = sum(cardPoints[:k])
        for i in range (k-1, -1, -1):
            total += cardPoints[i + len(cardPoints) - k] - cardPoints[i]
            best = max(best, total)
        return best
        
obj = Solution()
print(obj.maxScore([1,2,3,4,5,6,1],3))