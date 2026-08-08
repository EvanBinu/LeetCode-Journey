class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        def can(limit):
            groups = 1
            csum = 0
            for x in nums:
                if csum+x > limit:
                    groups+=1
                    csum =x
                else:
                    csum+=x
            return groups <=k
        while low<=high:
            mid = (low+high)//2
            if can(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low