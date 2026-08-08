class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2 = prev1 = 0
        for money in nums:
            c = max(prev1,money+prev2)
            prev2 = prev1
            prev1 = c
        return prev1