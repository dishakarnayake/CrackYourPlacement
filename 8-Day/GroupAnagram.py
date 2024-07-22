
from typing import List
from collections import defaultdict
class Solution(object):
   

    def getSignature(self, s) :
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, strs) :
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        result.extend(groups.values())

        return result


        