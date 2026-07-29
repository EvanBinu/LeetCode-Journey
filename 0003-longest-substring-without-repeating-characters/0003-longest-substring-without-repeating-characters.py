class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        maxcnt = 0
        n = len(s)
        for r in range(n):
            if s[r] in map and map[s[r]] >= left:
                left = map[s[r]] + 1
            map[s[r]] = r
            maxcnt = max(maxcnt,r - left + 1)
        return maxcnt 
