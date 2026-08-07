class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        left = 0
        mcount = 0
        for right in range(len(s)):
            if s[right] in "aeiou":
                count+=1
            if right >=k - 1:
                mcount = max(count,mcount)
                if s[left] in "aeiou":
                    count-=1
                left+=1
        return mcount