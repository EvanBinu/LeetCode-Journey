class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        while i < n and j < n:
            if nums[j]!=0:
                if i!=j:
                    nums[i] = nums[j]
                    nums[j] = 0
                i+=1
            j=j+1
            