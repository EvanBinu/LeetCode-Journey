class Solution:
    def helper(self,n):
        s = 0
        while n >0:
            d = n%10
            s+=d*d
            n//=10
        return s
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = self.helper(slow)
            fast = self.helper(self.helper(fast))
            if slow == 1:
                return True
            if slow==fast:
                return False
            