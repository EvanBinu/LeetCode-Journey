class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        val = 0
        while num > 0:
            d = num%10
            num//=10
            val = val*10+d
        return val == x
        