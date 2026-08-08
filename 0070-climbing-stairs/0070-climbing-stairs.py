class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return 1
        p = 1
        q = 2
        for i in range(3,n+1):
            r = p + q
            p = q
            q = r
        return q