class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        maxcnt = 0
        for right in range(len(s)):
            map[s[right]] = map.get(s[right],0) +1
            while map[s[right]] > 1:
                map[s[left]]-=1
                left+=1
            map[s[right]]=1
            maxcnt = max(maxcnt,right-left+1)
        return maxcnt 
