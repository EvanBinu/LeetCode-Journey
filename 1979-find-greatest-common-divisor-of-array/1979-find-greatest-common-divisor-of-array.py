class Solution:
    def helper(self,a,b):
        while b > 0:
            a,b = b,a%b
        return a
    def findGCD(self, nums: List[int]) -> int:
        mi = min(nums)
        ma = max(nums)
        return self.helper(mi,ma)