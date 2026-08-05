class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        total = sum(nums)
        for i in range(len(nums)):
            if total - prefix[i] == prefix[i] - nums[i]:
                return i
        return -1
        