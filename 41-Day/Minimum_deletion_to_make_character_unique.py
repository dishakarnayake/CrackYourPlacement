class Solution(object):
    def minDeletions(self, s):
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()
        
        for char, freq in cnt.items():
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            used_frequencies.add(freq)
            
        return deletions
        