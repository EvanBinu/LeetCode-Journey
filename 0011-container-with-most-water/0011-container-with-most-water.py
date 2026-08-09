class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        s = 0
        ms = 0
        l = 0
        r = n - 1
        while l<r:
            w = r - l
            s = w * min(height[l],height[r])
            ms = max(ms,s)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ms