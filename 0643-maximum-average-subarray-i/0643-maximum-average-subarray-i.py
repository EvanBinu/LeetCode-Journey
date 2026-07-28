class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sval = 0
        val = 0
        for i in range(k):
            sval+=nums[i]
        val = sval/k
        for i in range(k,len(nums)):
            sval = sval - nums[i-k]
            sval +=nums[i]
            val = max(val,sval/k)
        return val