class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for x in s:
            freq[x] = freq.get(x,0)+1
        index = -1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                index = i
                break
        return index