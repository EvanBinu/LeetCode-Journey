class Solution:
    def helper(self,nums,k):
        n = len(nums)
        seen = {}
        left = 0
        ans = 0
        for right in range(n):
            seen[nums[right]] = seen.get(nums[right],0)+1
            while len(seen) > k:
                seen[nums[left]]-=1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left+=1
            ans += right-left+1
        return ans
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k) - self.helper(nums,k-1)