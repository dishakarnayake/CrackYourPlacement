class Solution(object):
    def partition(self, s):
        self.n = len(s)
        res = []
        curr = []
        self.backTrack(s, 0, 1, curr, res)
        return res

    def backTrack(self, s, beg, len, curr, res):
        if beg == self.n:
            res.append(curr[:])
            return
        if beg + len > self.n:
            return

        self.backTrack(s, beg, len + 1, curr, res)

        if self.isPalindrome(s[beg:beg + len]):
            curr.append(s[beg:beg + len])
            self.backTrack(s, beg + len, 1, curr, res)
            curr.pop()  # Remove the last element to backtrack

    def isPalindrome(self, s):
        beg, end = 0, len(s) - 1
        while beg < end:
            if s[beg] != s[end]:
                return False
            beg += 1
            end -= 1
        return True