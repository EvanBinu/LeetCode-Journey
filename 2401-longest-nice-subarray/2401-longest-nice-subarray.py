class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        ms = 0
        mask = 0
        for right in range(len(nums)):
            while mask & nums[right]:
                mask^=nums[left]
                left+=1
            mask|=nums[right]
            ms = max(ms,right-left+1)
        return ms

