from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp = deque()
        ans = []
        for i in range(len(nums)):
            while dp and dp[0] <= i-k:
                dp.popleft()
            while dp and nums[dp[-1]] <= nums[i]:
                dp.pop()
            dp.append(i)
            if i >= k-1:
                ans.append(nums[dp[0]])
        return ans