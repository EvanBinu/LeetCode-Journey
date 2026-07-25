class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        i = 0
        j = n - 1
        k = n - 1
        while i <= j:
            v1 = nums[i] * nums[i]
            v2 = nums[j] * nums[j]
            if(v1 >= v2):
                ans[k] = v1
                k-=1
                i+=1
            else:
                ans[k] = v2
                k-=1
                j-=1
        return ans
                
                
