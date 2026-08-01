class Solution:
    def helper(self,n):
        s = 0
        while n >0:
            d = n%10
            s+=d*d
            n//=10
        return s
    def isHappy(self, n: int) -> bool:
        cycle = []
        s = 0
        while s!=1:
            s = self.helper(n)
            if s in cycle:
                return False
            if s==1:
                return True
            cycle.append(s)
            n = s