class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = {0:1}
        prefix = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix == 0:
                maxlen = i + 1
            if prefix in freq:
                maxlen = max(maxlen,i-freq[prefix])
            if prefix not in freq:
                freq[prefix] = i
        return maxlen
