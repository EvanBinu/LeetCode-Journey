class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can(dist):
            count = 1
            last = position[0]
            for i in range(1,len(position)):
                if position[i] - last >=dist:
                    count+=1
                    last = position[i]
                    if count == m :
                        return True
            return False
        low = 1
        high = position[-1] - position[0]
        answer = 0
        while low <=high:
            mid = (low+high)//2
            if can(mid):
                answer= mid
                low=mid+1
            else:
                high=mid-1
        return answer