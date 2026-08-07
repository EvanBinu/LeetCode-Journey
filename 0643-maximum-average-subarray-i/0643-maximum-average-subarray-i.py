class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        s = 0
        avg = float("-inf")
        for right in range(len(nums)):
            s+=nums[right]
            if right >= k - 1:
                avg=max(s/k,avg)
                s-=nums[left]
                left+=1
        return avg


