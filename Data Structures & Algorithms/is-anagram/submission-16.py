class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq2 = {}
        for x in s:
            freq[x] = freq.get(x, 0) + 1
        for i in t:
            freq2[i] = freq2.get(i, 0) + 1
        if freq == freq2:
            return True
        return False
