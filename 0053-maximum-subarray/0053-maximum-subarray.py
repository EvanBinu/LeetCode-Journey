class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        mcurr = 0
        pos = False
        for x in nums:
            if x > 0:
                pos = True
        if pos == False:
            return max(nums)
        else:
            for i in range(len(nums)):
                curr += nums[i]
                if(curr < 0):
                    curr = 0
                mcurr = max(curr,mcurr)
            return mcurr
        