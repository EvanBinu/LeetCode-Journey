class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        map1 = [0]*26
        map2 = [0]*26
        left = 0
        for i in range(k):
            map1[ord('a') - ord(s1[i])]+=1
        for j in range(n):
            map2[ord('a') - ord(s2[j])]+=1
            if (j - left + 1) ==k:
                if map1 == map2:
                    return True
                map2[ord('a') - ord(s2[left])]-=1
                left+=1
        return False 