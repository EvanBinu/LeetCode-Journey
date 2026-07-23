class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        left = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= left:
                left = dict[s[i]] + 1
            
            dict[s[i]] = i
            maxlen = max(maxlen,i-left+1)
        return maxlen
        