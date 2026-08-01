class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        num = abs(x)
        rev = 0
        while num > 0:
            d = num%10
            num//=10
            rev = rev*10+d
        rev = -rev if neg else rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev