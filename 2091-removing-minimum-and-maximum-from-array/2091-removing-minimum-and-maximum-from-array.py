class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mini = nums.index(min(nums)) 
        maxi = nums.index(max(nums))
        left = min(mini,maxi)
        right = max(mini,maxi)
        return min(right + 1, n - left , (left+1 +( n -right) ))