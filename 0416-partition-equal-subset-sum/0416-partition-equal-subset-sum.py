class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        capacity = sum(nums)
        if capacity%2!=0:
            return False
        else:
            c = capacity//2
        dp = [False] * (c + 1)
        dp[0] = True
        for num in nums:
            for i in range(c,num-1,-1):
                dp[i] = dp[i] or dp[i - num]
        return dp[c]