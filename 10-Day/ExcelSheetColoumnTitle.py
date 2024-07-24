class Solution:
    def convertToTitle(self, columnNumber):
        base = 26
        ans = ""

        power = 0
        while columnNumber > 0:
            factor = base**power
            char = int((columnNumber/(factor))%base)
            char = 26 if char == 0 else char
            ans = 'Z' + ans if char == 26 else chr(64+char) + ans
            columnNumber = columnNumber-(char*(factor))
            power += 1
            
        return ans
    
obj = Solution()
print(obj.convertToTitle(555))