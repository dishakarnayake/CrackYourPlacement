class Solution(object):
    def removeKdigits(self, num, k):
        stk = []
        ans = ""
        for c in num:
            while k > 0 and stk and stk[-1] > c:
                stk.pop()
                k -= 1
            stk.append(c)
        while k > 0:
            stk.pop()
            k -= 1
        for c in stk:
            if not ans and c == '0':
                continue
            ans += c
        return ans if ans else '0'
        