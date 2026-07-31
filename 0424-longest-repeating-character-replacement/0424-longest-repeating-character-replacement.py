class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxlen = 0
        maxfreq = 0
        left = 0
        map = {}
        for right in range(n):
            map[s[right]] = map.get(s[right],0)+1
            maxfreq = max(maxfreq,map[s[right]])
            if (right-left+1) - maxfreq > k:
                if s[left] in map:
                    map[s[left]]-=1
                if map[s[left]]==0:
                    del map[s[left]]
                left+=1
            maxlen = max(maxlen,right-left+1)
        return maxlen
