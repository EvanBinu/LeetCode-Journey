class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow  = fast = 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast+=1
            else:
                nums[slow+1] = nums[fast]
                slow+=1
        return slow+1
