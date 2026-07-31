class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minlen = float('inf')
        s = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                minlen = min(minlen, right-left+1)
                s -= nums[left]
                left += 1
        return 0 if minlen == float('inf') else minlen