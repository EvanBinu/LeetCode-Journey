class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        mlen = 0
        for right in range(len(s)):
            map[s[right]] = map.get(s[right],0)+1
            while map[s[right]] > 1:
                map[s[left]]-=1
                left+=1
            mlen = max(mlen,right-left+1)
        return mlen