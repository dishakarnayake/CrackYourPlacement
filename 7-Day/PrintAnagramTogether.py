class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        d={}
        for word in words:
            sorted_word="".join(sorted(word))
            if d.get(sorted_word):
                d[sorted_word].append(word)
            else:
                d[sorted_word]=[word]
        return d.values()
    
obj = Solution()
print(obj.Anagrams(["eat", "tea", "tan", "ate", "nat", "bat"], 6))