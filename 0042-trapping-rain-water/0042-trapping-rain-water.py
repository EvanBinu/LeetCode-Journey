class Solution:
    def trap(self, height: List[int]) -> int:
        lm = rm = l = 0
        n = len(height)
        r = n - 1
        water = 0
        while l < r:
            if height[l] <= height[r]:
                lm = max(lm,height[l])
                water += lm - height[l]
                l+=1
            else:
                rm = max(rm,height[r])
                water += rm - height[r]
                r-=1
        return water