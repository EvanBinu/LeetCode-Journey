class Solution:
    def helper(self,arr,k):
        n = len(arr)
        s = 0
        left = 0
        ans = 0
        for right in range(n):
            s += arr[right]
            while s > k:
                s-=arr[left]
                left+=1
            ans += right-left+1
        return ans
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = []
        for x in nums:
            if x%2!=0:
                arr.append(1)
            else:
                arr.append(0)
        return self.helper(arr,k) - self.helper(arr,k-1)
        
