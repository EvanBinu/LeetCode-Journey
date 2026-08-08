class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n):
            if farthest < i:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
        return True