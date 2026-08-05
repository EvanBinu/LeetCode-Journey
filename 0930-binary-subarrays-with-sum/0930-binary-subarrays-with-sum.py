class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0:1}
        prefix=  0
        answer = 0
        for num in nums:
            prefix+=num
            if prefix-goal in freq:
                answer+=freq[prefix-goal]
            freq[prefix] = freq.get(prefix,0)+1
        return answer