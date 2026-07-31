class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map ={}
        maxfreq=0
        maxlen = 0
        left = 0
        for right in range(len(s)):
            if s[right] in map:
                map[s[right]]+=1
            else:
                map[s[right]] =1 
            maxfreq = max(maxfreq,map[s[right]])
            if (right-left+1) - maxfreq > k:
                map[s[left]]-=1
                left+=1
            maxlen=  max(maxlen,right-left+1)
        return maxlen