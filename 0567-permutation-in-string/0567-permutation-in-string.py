class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        freq1 = [0]*26
        freq2 = [0]*26
        left = 0
        for i in range(k):
            freq1[ord('a')-ord(s1[i])]+=1
        for right in range(n):
            freq2[ord('a')-ord(s2[right])]+=1
            if (right - left + 1) >= k:
                if freq1==freq2:
                    return True
                freq2[ord('a')-ord(s2[left])]-=1
                left+=1
        return False