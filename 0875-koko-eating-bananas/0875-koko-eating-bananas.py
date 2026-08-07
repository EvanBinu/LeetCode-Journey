class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        count = float("inf")
        while low <= high:
            mid = (low+high)//2
            s = 0
            for x in piles:
                s+=(x+mid-1)//mid
            if s <= h:
                high = mid - 1
                count = min(count,mid)
            else:
                low = mid+1
        return count