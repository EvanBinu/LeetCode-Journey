class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        val = high
        while low <=high:
            mid = (low+high)//2
            s = 1
            d = 0
            for x in weights:
                if d+x > mid:
                    s+=1
                    d = x
                else:
                    d+=x
            if s <=days:
                val = min(mid,val)
                high = mid - 1
            else:
                low = mid + 1            
        return val