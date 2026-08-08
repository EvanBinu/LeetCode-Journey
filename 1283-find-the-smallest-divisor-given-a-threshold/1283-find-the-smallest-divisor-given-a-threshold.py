class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        val = float("inf")
        while low <=high:
            mid = (low+high)//2
            s  = sum((x + mid - 1)//mid for x in nums)
            if s <=threshold:
                val = min(val,mid)
                high = mid - 1
            else:
                low = mid + 1
        return val